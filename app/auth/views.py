# coding:utf-8
from flask import render_template, redirect, request, flash, url_for
from . import auth		# blueprint
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, RegistrationForm, UpdatePasswordForm, EditForm
from ..models import User
from .. import db

# @auth.before_app_request
# def before_request():
# 	if not current_user.is_authenticated:
# 		if request.endpoint \
# 				and request.endpoint[:5] != 'auth.' \
# 				and request.endpoint != 'static':
# 			return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(name=form.name.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))
		flash('用户名或密码不正确')
	return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(name=form.name.data, 
					password=form.password.data)
		db.session.add(user)
		# db.session.commit()		# 要立即提交数据库，因为后面的操作需要提交后自动生成的 id 字段
		try:
			db.session.commit()
		except:
			db.session.rollback()
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)


@auth.route('/password/update', methods=['GET','POST'])
@login_required
def update_password():
	"""更改密码(已知旧密码)"""
	form = UpdatePasswordForm()
	if form.validate_on_submit():
		if not current_user.verify_password(form.old_password.data):
			flash('your old password is not right! Please try again!')
			return redirect(url_for('.update_password'))
		if current_user.update_password(form.new_password.data):	# 如果更新密码成功
			logout_user()			# 登出现有用户，重新登录
			flash('you have changed your password, please login')
			return redirect(url_for('.login'))
		else:
			flash('failed to update your password, please try again')
	return render_template('auth/password/update.html', form = form)







