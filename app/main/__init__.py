# coding:utf-8
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors, util
from .. import db

# 将此函数注入到各个template中
@main.context_processor
def inject_func():
	return dict(get_distance=util.get_distance)	# 根据经纬度信息计算两点间距离

@main.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()