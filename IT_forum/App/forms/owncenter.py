from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileRequired,FileField
from wtforms import SubmitField,StringField,RadioField
from wtforms.validators import DataRequired
from App.extensions import file

class UploadPhotos(FlaskForm):
    photo = FileField('',validators=[DataRequired(message=' '),FileAllowed(file,message='只能上传图片')])
    submit = SubmitField("上传")
class UploadInfo(FlaskForm):
    sex = RadioField('性别', choices=[('m', '男'), ('w', '女')])
    age = StringField('年龄',render_kw={'placeholder':'请输入您的年龄','maxlength':2})#validators=[DataRequired(message='请输入您的年龄')],
    submit = SubmitField("确认修改")

class SubmitInfo(FlaskForm):
    submit = SubmitField("提交")