from flask import Blueprint,render_template,redirect,request,current_app,url_for
from App.models import Posts,User,Course
from App.extensions import cache#缓存
from datetime import datetime,timedelta
from flask_login import current_user
from  sqlalchemy import and_,not_
import os
main = Blueprint('main',__name__)

@main.route('/')
def index():
    return redirect(url_for('main.show',page=1))

@main.route('/show/<int:page>/')
@cache.memoize(timeout=10)
def show(page):
    print('-----------------------------------------------------')
    print(os.path.abspath(os.path.dirname(__file__)))
    pagination = Posts.query.filter_by(pid=0).order_by(Posts.timestamp.desc()).paginate(page, current_app.config[
        'EVERY_PAGE_NUM'], False)
    data = pagination.items
    # print(len(data))
    # u = User.query.filter_by(id=1).first()
    # u.register_date = datetime.utcnow()-timedelta(hours=240)
    # u.save()
    if current_user.is_authenticated:
        title = current_user.username
    else:
        title = '请登录后访问'
    now = datetime.utcnow()+timedelta(hours=8)
    ##############课程############################
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','),Course.pid!=0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')),Course.pid!=0))
    for i in c2:
        print(i)
    # print(c)
    return render_template('main/index.html', data=data, pagination=pagination,now=now,title=title,course=c,course1=c1,course2=c2)
