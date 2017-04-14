from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, BooleanField, PasswordField, SubmitField, TextField
from wtforms.validators import Required, Length, Regexp, EqualTo
from wtforms import ValidationError
from flask_uploads import UploadSet, IMAGES

from app.models import User

images = UploadSet('images', IMAGES)

class LoginForm(FlaskForm):
	name = StringField('昵称', validators=[Required(), Length(1,64)])
	password = PasswordField('密码', validators=[Required()])
	remember_me = BooleanField('保持登录状态')
	submit = SubmitField('登录')

class RegistrationForm(FlaskForm):
	name = StringField('昵称', validators=[Required(), Length(1,64),
										Regexp('^[a-zA-Z][a-zA-Z0-9_.]*$',0,'昵称只能包含数字，字母，_ ，. ')])
	password = PasswordField('密码', validators=[Required(), EqualTo('password2', '密码不匹配')])
	password2 = PasswordField('确认密码', validators=[Required()])
	submit = SubmitField('注册')

	def validate_username(self, field):
		if User.query.filter_by(name=field.data).first():
			raise ValidationError('昵称已经被占用')

class UpdatePasswordForm(FlaskForm):
	old_password = PasswordField('旧密码', validators=[Required()])
	new_password = PasswordField('新密码', validators=[Required(), EqualTo('new_password2', '密码不匹配')])
	new_password2 = PasswordField('确认新密码', validators=[Required()])
	submit = SubmitField('确认修改')

class EditForm(FlaskForm):
	name = StringField('昵称', validators=[Required(), Length(1,64),
										Regexp('^[a-zA-Z][a-zA-Z0-9_.]*$',0,'昵称只能包含数字，字母，_ ，. ')])
	pic = FileField('上传头像', validators=[FileRequired('文件未选择！'),FileAllowed(['jpg', 'png'], '只能上传图片')])
	describe = TextField('个人简介')
	wechat_id = StringField('微信号')
	wechat_qr = FileField('微信二维码', validators=[FileRequired('文件未选择！'),FileAllowed(['jpg', 'png'], '只能上传图片')])
	submit = SubmitField('确认编辑')







