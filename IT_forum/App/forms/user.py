from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_uploads import UploadSet,IMAGES
from App.models import User


file = UploadSet('image', IMAGES)
class Register(FlaskForm):
    username = StringField('请输入用户名',validators=[DataRequired(message='用户名不能为空'),Length(min=4,max=12,message='用户名必须是4-12位')],render_kw={'placeholder':'请输入用户名','maxlength':12})
    userpass = PasswordField('请输入密码',validators=[DataRequired(message='密码不能为空'),Length(min=6,max=12,message='密码必须是6-12位')],render_kw={'placeholder':'请输入密码','maxlength':12})
    confirm = PasswordField('请再次输入密码',validators=[EqualTo('userpass',message='两次输入的密码不一致')],render_kw={'placeholder':'请输入密码','maxlength':12})
    email = StringField('请输入邮箱帐号',validators=[DataRequired(),Length(min=6,max=50,message='111'),Email(message='请输入正确邮箱')],render_kw={'placeholder':'请输入邮箱','maxlength':50})
    # uploadfile = FileField('上传头像',validators=[FileRequired(message='请上传头像'),FileAllowed(file,message='文件格式不正确')])
    # uploadfile = FileField('上传头像')
    submit = SubmitField('注册')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户已存在')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在')

#登录表单
class Login(FlaskForm):
    username = StringField('请输入用户名',
                           validators=[DataRequired(message='用户名不能为空'), Length(min=4, max=12, message='用户名必须是4-12位')],
                           render_kw={'placeholder': '请输入用户名', 'maxlength': 12})
    userpass = PasswordField('请输入密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=12, message='密码必须是6-12位')],
                             render_kw={'placeholder': '请输入密码', 'maxlength': 12})
    submit = SubmitField('登录')
#激活用户
class AgainActivate(FlaskForm):
    username = StringField('请输入用户名',
                           validators=[DataRequired(message='用户名不能为空'), Length(min=4, max=12, message='用户名必须是6-12位')],
                           render_kw={'placeholder': '请输入用户名', 'maxlength': 12})
    userpass = PasswordField('请输入密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=12, message='密码必须是6-12位')],
                             render_kw={'placeholder': '请输入密码', 'maxlength': 12})
    submit = SubmitField('激活')

    def validate_username(self, field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('激活用户不存在')

#修改密码
class Modify_code(FlaskForm):
    userpass = PasswordField('请输入原始密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=12, message='密码必须是6-12位')],
                             render_kw={'placeholder': '请输入密码', 'maxlength': 12})
    userpass1 = PasswordField('请输入新密码',
                             validators=[DataRequired(message='密码不能为空'), Length(min=6, max=12, message='密码必须是6-12位')],
                             render_kw={'placeholder': '请输入密码', 'maxlength': 12})
    userpass2 = PasswordField('请再次输入新密码',
                             validators=[EqualTo('userpass1',message='两次输入的密码不一致'),Length(min=6, max=12, message='密码必须是6-12位')],
                             render_kw={'placeholder': '请输入密码', 'maxlength': 12})
    submit = SubmitField('确认修改')
#修改邮箱
class Modify_email(FlaskForm):
    email = StringField('请输入新的邮箱帐号',validators=[DataRequired(),Length(min=6,max=50,message='111'),Email(message='请输入正确邮箱')],render_kw={'placeholder':'请输入邮箱','maxlength':50})
    submit = SubmitField('确认修改')