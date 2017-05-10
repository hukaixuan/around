# coding:utf-8
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

from .. import db

# @auth.teardown_appcontext
# def shutdown_session(exception=None):
#     db.session.remove()
