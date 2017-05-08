# coding:utf-8
from flask import render_template, flash, redirect, url_for, current_app, request, session, \
					abort
from . import main
from ..models import User, Post, Label, Comment
from .. import db
from flask_login import login_required, current_user
from .forms import EditProfileForm, PostForm, CommentForm
import os
import time
import hashlib
from datetime import datetime

from .util import process_img

@main.route('/')
def index():
	posts = Post.query.all()
	return render_template('index.html', posts=posts)

@main.route('/save_location', methods=['POST'])
def save_location():
	if request.method == 'POST':
		session['longitude'] = request.form.get('longitude')
		session['latitude'] = request.form.get('latitude')
		return '定位成功'

@main.route('/user/<name>')
def user(name):
	user = User.query.filter_by(name=name).first_or_404()
	posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).all()
	return render_template('user.html', user=user, posts=posts)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.name = form.name.data
		if form.pic.data:
			f = form.pic.data
			filename = hashlib.md5((current_user.name + str(time.time())).encode('utf-8')).hexdigest()
			filename = filename + '.' + extension(f.filename)
			pic_path = os.path.join(current_app.config['PIC_PATH'], filename)
			pic_save = os.path.join(current_app.root_path, 'static', pic_path)
			f.save(pic_save)
			process_img(pic_save)
			current_user.pic = pic_path
			
		current_user.describe = form.describe.data
		current_user.wechat_id = form.wechat_id.data

		if form.wechat_qr.data:
			f = form.wechat_qr.data
			filename = hashlib.md5((current_user.name + str(time.time())).encode('utf-8')).hexdigest()
			filename = filename + '.' + extension(f.filename)
			# 数据库存储的图片路径
			wechat_qr_path = os.path.join(current_app.config['PIC_PATH'], filename)
			# 图片保存路径
			wechat_qr_save = os.path.join(current_app.root_path, 'static', wechat_qr_path)
			f.save(wechat_qr_save)	
			process_img(wechat_qr_save)	
			current_user.wechat_qr = wechat_qr_path
			
		db.session.add(current_user)
		return redirect(url_for('.user', name=current_user.name))
	form.name.data = current_user.name
	form.pic.data = current_user.pic
	form.describe.data = current_user.describe
	form.wechat_id.data = current_user.wechat_id
	form.wechat_qr.data = current_user.wechat_qr
	return render_template('edit_profile.html', form=form)

# 添加文件后缀
def extension(filename):
	ext = os.path.splitext(filename)[1]
	if ext == '':
		ext = os.path.splitext(filename)[0]
	if ext.startswith('.'):
		# os.path.splitext retains . separator
		ext = ext[1:]
	return ext


@main.route('/get_post/<int:id>', methods=['GET','POST'])
def get_post(id):
	post = Post.query.get_or_404(id)
	form = CommentForm()
	if form.validate_on_submit():
		content = form.content.data
		comment = Comment(post_id=post.id, user_id=current_user.id,\
					 content=content, timestamp=datetime.utcnow())
		db.session.add(comment)
		return redirect(url_for('main.get_post', id=post.id))
	comments = Comment.query.filter_by(post_id=post.id).order_by(Comment.timestamp.desc()).all()
	return render_template('get_post.html', post=post, comments=comments, form=form)

@main.route('/post', methods=['GET','POST'])
@login_required
def post():
	form = PostForm()
	if form.validate_on_submit():
		label_id = form.label.data
		content = form.content.data
		post = Post(label_id=label_id, content=content, 
			longitude= session.get('longitude'), latitude= session.get('latitude'),
			user_id=current_user.id, timestamp=datetime.utcnow())
		db.session.add(post)
		return redirect(url_for('main.index'))
	return render_template('post.html', form=form)

@main.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
	post = Post.query.get_or_404(post_id)
	if current_user.id != post.user_id:
		abort(403)
	form = PostForm()
	if form.validate_on_submit():
		post.label_id = form.label.data
		post.content = form.content.data
		db.session.add(post)
		flash('修改成功')
		return redirect(url_for('main.user', name=current_user.name))
	form.label.data = post.label_id
	form.content.data = post.content
	return render_template('edit_post.html', form=form)

@main.route('/delete_post/<int:post_id>')
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	if current_user.id != post.user_id:
		abort(403)
	db.session.delete(post)
	return redirect(url_for('main.user', name = current_user.name))

@main.route('/edit_comment/<int:id>', methods=['GET', 'POST'])
def edit_comment(id):
	comment = Comment.query.get_or_404(id)
	if current_user.id != comment.user_id:
		abort(403)
	form = CommentForm()
	if form.validate_on_submit():
		comment.content = form.content.data
		db.session.add(comment)
		return redirect(url_for('main.get_post', id=comment.post.id))
	form.content.data = comment.content
	return render_template('edit_comment.html', form=form)

@main.route('/delete_comment/<int:id>')
def delete_comment(id):
	comment = Comment.query.get_or_404(id)
	if current_user.id != comment.user_id:
		abort(403)
	id = comment.post.id
	db.session.delete(comment)
	return redirect(url_for('main.get_post', id=id))

@main.route('/search')
@main.route('/search/<label_id>')
def search(label_id=None):
	labels = Label.query.all()
	posts_query = Post.query.order_by(Post.timestamp.desc())
	posts = posts_query.filter_by(label_id=label_id).all() if label_id \
				else posts_query.all()
	return render_template('search.html', label_id=int(label_id) if label_id else 0, labels=labels, posts=posts )


@main.route('/test')
def test():
	id = User.query.first().id
	return str(id)












