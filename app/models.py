# coding:utf-8
from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
	# __table__ = db.Model.metadata.tables['user']
	__tablename__ = 'user'
	
	@property
	def password(self):
		raise AttributeError("password is not a readable attribute")

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		"""确认密码是否正确"""
		return check_password_hash(self.password_hash, password)

	def update_password(self, new_password):
		"""更新密码"""
		self.password = new_password
		db.session.add(self)
		return True

	# 获取该用户发布的所有内容
	@property
	def posts(self):
		return Post.query.filter_by(user_id=self.id).all()


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))



class Post(db.Model):
	# __table__ = db.Model.metadata.tables['post']
	__tablename__ = 'post'

	# 获取发布者
	@property
	def user(self):
		return User.query.filter_by(id=self.user_id).first()

	# 获取该post的label
	@property
	def label(self):
		return Label.query.filter_by(id=self.label_id).first()



class Label(db.Model):
	__table__ = db.Model.metadata.tables['label']

	# 获取该label 下的所有 post
	@property
	def posts(self):
		return Post.query.filter_by(label_id=self.id).all()

class Comment(db.Model):
	__tablename__ = 'comment'

	# 获取该comment对应的post
	@property
	def post(self):
		return Post.query.filter_by(id=self.post_id).first()

	# 获取发布该评论的user
	@property
	def user(self):
		return User.query.filter_by(id=self.user_id).first()








