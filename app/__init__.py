# coding:utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
moment = Moment()

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
	app = Flask(__name__)
	# 在form.py使用db及model报错：RuntimeError: application not registered on db instance and no applicationbound to current context
	# 在https://blog.tonyseek.com/post/the-context-mechanism-of-flask/启发下加了这两行就OK了
	ctx = app.app_context()
	ctx.push()

	app.config.from_object(config[config_name])	# 从config.py根据传入的config_name选取对应的class进行配置
	config[config_name].init_app(app)	#init_app是干啥的？？？啥作用？
	bootstrap.init_app(app)
	db.init_app(app)
	moment.init_app(app)
	# with app.app_context():
	# 	db.Model.metadata.reflect(db.engine)
	op = getattr(db.Model.metadata, 'reflect')
	op(bind=db.get_engine(app), views=True)
	
	login_manager.init_app(app)

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')

	return app