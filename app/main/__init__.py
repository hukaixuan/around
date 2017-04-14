from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors, util

# 将此函数注入到各个template中
@main.context_processor
def inject_func():
	return dict(get_distance=util.get_distance)	# 根据经纬度信息计算两点间距离
