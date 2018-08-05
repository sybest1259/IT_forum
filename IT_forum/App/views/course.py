from flask import jsonify,Blueprint,request,render_template,redirect,url_for,flash,current_app
from App.forms import Course_main,Course_secondary,Course_third
from App.models import Course
from flask_login import current_user
from datetime import datetime,timedelta
from App.extensions import cache

from sqlalchemy import and_,not_
course = Blueprint('course',__name__)
@course.route('/course/index/',methods=['GET','POST'])
def index():
    c = Course.query.all()
    print(c)
    return render_template('main/index.html')
@course.route('/course/add_main/',methods=['GET','POST'])
def add_course_main():
    form = Course_main()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            c = Course(title=form.title.data,abstract=form.abstract.data,timestamp=datetime.utcnow()+timedelta(hours=8))
            print(c.timestamp)
            c.save()
            flash('创建课程分类成功')
            cache.clear()#因为数据库更新,页面也需要更新，所以需要清除所有缓存
            return redirect(url_for('main.index'))
        else:
            print(1)
            flash('您还没登录')
            return redirect(url_for('user.login'))
    if not current_user.is_authenticated:
        print(2)
        flash('您还没登录 请登录后发表')
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('course/add_main.html',form=form,course=c,course1=c1,course2=c2)
@course.route('/course/add_secondary/<course>',methods=['GET','POST'])
def add_course_secondary(course):
    print('_________________________________________________________')
    print(course)
    id = course.split(' ')[1].split('>')[0]
    parent = Course.query.filter_by(id=id).first()
    form = Course_secondary()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            c = Course(pid=id,path=parent.path+id+',',title=form.title.data,timestamp=datetime.utcnow()+timedelta(hours=8))
            print(c.timestamp)
            c.save()
            flash('创建课程章节成功')
            cache.clear()#因为数据库更新,页面也需要更新，所以需要清除所有缓存
            return redirect(url_for('main.index'))
        else:
            print(1)
            flash('您还没登录')
            return redirect(url_for('user.login'))
    if not current_user.is_authenticated:
        print(2)
        flash('您还没登录 请登录后发表')
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('course/add_secondary.html',form=form,course=c,course1=c1,course2=c2)
@course.route('/course/add_third/<course>',methods=['GET','POST'])
def add_course_third(course):
    print('_________________________________________________________')
    print(course)
    id = course.split(' ')[1].split('>')[0]
    parent = Course.query.filter_by(id=id).first()
    form = Course_third()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            c = Course(pid=id,path=parent.path+id,title=form.title.data,timestamp=datetime.utcnow()+timedelta(hours=8))
            print(c.timestamp)
            c.save()
            flash('创建课程成功')
            cache.clear()#因为数据库更新,页面也需要更新，所以需要清除所有缓存
            return redirect(url_for('course.add_course_third',course=course))
        else:
            print(1)
            flash('您还没登录')
            return redirect(url_for('user.login'))
    if not current_user.is_authenticated:
        print(2)
        flash('您还没登录 请登录后发表')
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','),Course.pid!=0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')),Course.pid!=0))
    return render_template('course/add_third.html',form=form,course=c,course1=c1,course2=c2)
@course.route('/course/show_course/<title>')
def show_course(title):
    if current_user.is_authenticated:
        c = Course.query.filter_by(pid=0)
        c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
        c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
        return render_template('course/show_course.html',title=title,course=c,course1=c1,course2=c2)
    else:
        flash('请登录后观看')
        return redirect(url_for('user.login'))