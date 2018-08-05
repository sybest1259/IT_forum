from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length
from wtforms import SubmitField,StringField,TextAreaField


class Course_main(FlaskForm):
    title = StringField('课程分类名称',validators=[DataRequired(message='内容不能为空'),Length(min=2,max=30,message='内容长度为2-30个字符')],render_kw={'placeholder':'请输入课程分类名称','maxlength':30})
    abstract = TextAreaField('课程简介',validators=[DataRequired(message='内容不能为空'),Length(min=10,max=2000,message='课程简介长度为10-2000个字符')],render_kw={'placeholder':'请输入课程简介','maxlength':2000})
    submit = SubmitField("提交")
class Course_secondary(FlaskForm):
    title = StringField('课程章节名称',validators=[DataRequired(message='内容不能为空'),Length(min=3,max=3,message='内容长度为3个字符')],render_kw={'placeholder':'请输入课程章节名称(第一章)','maxlength':3})
    submit = SubmitField("提交")
class Course_third(FlaskForm):
    title = StringField('课程名称',validators=[DataRequired(message='内容不能为空'),Length(min=2,max=20,message='内容长度为2-20个字符')],render_kw={'placeholder':'请输入课程名称','maxlength':20})
    submit = SubmitField("提交")


