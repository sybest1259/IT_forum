from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length
from wtforms import SubmitField,StringField,TextAreaField


class SendPosts(FlaskForm):
    articletitle = StringField('标题',validators=[DataRequired(message='标题不能为空'),Length(min=5,max=30,message='标题长度为5-30个字符')],render_kw={'placeholder':'请输入标题','maxlength':30})
    article = TextAreaField('内容',validators=[DataRequired(message='内容不能为空'),Length(min=10,max=2000,message='文章长度为10-2000个字符')],render_kw={'placeholder':'请输入文章','maxlength':2000})
    submit = SubmitField("发表")
class SendDiscuss(FlaskForm):
    article = TextAreaField('评论内容',validators=[DataRequired(message='内容不能为空'),Length(min=10,max=2000,message='文章长度为10-2000个字符')],render_kw={'placeholder':'请输入文章','maxlength':2000})
    submit = SubmitField("发表")