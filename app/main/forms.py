from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextAreaField, SelectField, DateTimeField
from wtforms.validators import Required, Length, Regexp, EqualTo
from wtforms import ValidationError
from flask_uploads import UploadSet, IMAGES
from ..models import Label
from .. import db


images = UploadSet('images', IMAGES)

class EditProfileForm(FlaskForm):
	name = StringField('昵称', validators=[Required(), Length(1,64),
										Regexp('^[a-zA-Z][a-zA-Z0-9_.]*$',0,'昵称只能包含数字，字母，_ ，. ')])
	pic = FileField('上传头像', validators=[FileAllowed(['jpg', 'png'], '只能上传图片')])
	describe = TextAreaField('个人简介')
	wechat_id = StringField('微信号')
	wechat_qr = FileField('微信二维码', validators=[FileAllowed(['jpg', 'png'], '只能上传图片')])
	submit = SubmitField('确认编辑')

class PostForm(FlaskForm):
	label = SelectField('选择一个分类', coerce=str, choices=[(str(label.id), str(label.name)) for label in Label.query.all()])
	# label = SelectField('选择一个分类', choices=[(db.engine, db.session)])
	# start_time = DateTimeField('开始时间')
	# stop_time = DateTimeField('结束时间')
	content = TextAreaField('详细信息')
	submit = SubmitField('确定')

class CommentForm(FlaskForm):
	content = TextAreaField('评论')
	submit = SubmitField('提交')


