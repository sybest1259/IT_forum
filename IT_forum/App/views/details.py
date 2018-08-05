from flask import Blueprint,redirect,render_template,request,current_app,flash,url_for
from App.models import Posts,Course
from App.forms import SendDiscuss
from flask_login import current_user
from datetime import datetime,timedelta
from App.extensions import cache
from sqlalchemy import not_,and_

details = Blueprint('details',__name__)
@details.route('/details/<posts>')
def index(posts):
    return redirect(url_for('details.get_details',posts=posts,page=1))

@details.route('/details/<int:page>/<posts>',methods=['GET','POST'])
def get_details(page,posts):
    now = datetime.utcnow() + timedelta(hours=8)
    print(11111111111111111111111111111111111111111111111111111111111)
    #获取帖子id
    id = posts.split(' ')[1].split('>')[0]
    #浏览量设置###########
    p = Posts.query.filter_by(id=id).first()
    if p.scan:
        p.scan += 1
        p.save()
    else:
        p.scan = 1
        p.save()
    ####################
    pagination = Posts.query.filter_by(id=id).paginate(1, current_app.config[
        'EVERY_PAGE_NUM'], False)
    data = pagination.items#找到当前点击的帖子的数据
    pagination1 = Posts.query.filter(Posts.path.endswith(id+',')).order_by(Posts.timestamp.asc()).paginate(page, current_app.config['EVERY_PAGE_NUM'], False)
    data1 = pagination1.items#找到当前点击的帖子的所有回复帖子数据
    #找到pid=回复帖子id的数据
    list_anwser = []
    list_anwser_list = []
    for i in Posts.query.filter(Posts.path.endswith(id+',')).order_by(Posts.timestamp.asc()):#找到当前点击的帖子的所有回复帖子数据
        #i为每条回复，answer为每条回复的回复的集合
        anwser = Posts.query.filter(Posts.path.endswith(str(i.id) + ',')).order_by(Posts.timestamp.asc())
        #list_anwser为所有回复的回复的集合
        list_anwser_list.append(anwser.all())
        list_anwser.append(anwser)
    # print(page)
    # print(len(data1))
    # for i in data1:
    #     print(i)
    # print(len(list_anwser))
    # for i in list_anwser:
    #     print(i)
    # print(Posts.query.filter_by(id=id).first().user)
    # # print(Posts.query.filter_by(id=id).first().users)
    # for i in Posts.query.filter_by(id=id).first().users:
    #     print(i)
    # print(type(current_user.favorite))
    # print(current_user.favorite.all())
    # for i in current_user.favorite:
    #     print(i)
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('posts/details.html',data=data,data1=data1,pagination=pagination1,list_anwser=list_anwser,list_anwser_list=list_anwser_list,now=now,course=c,course1=c1,course2=c2)


@details.route('/details/discuss/<posts>',methods=['GET','POST'])
def discuss(posts):
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    ##########################################################################
    form = SendDiscuss()
    id = posts.split(' ')[1].split('>')[0]
    parent = Posts.query.filter_by(id=id).first()
    title = '回复'+parent.user.username+'：'
    grandparent = Posts.query.filter_by(id=parent.pid).first()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            p = Posts(pid=id,path=parent.path+id+',',title=title,article=form.article.data,user=current_user,timestamp=datetime.utcnow()+timedelta(hours=8))
            p.save()
            flash('发表成功')
            cache.clear()#因为数据库更新,页面也需要更新，所以需要清除所有缓存
            if grandparent:
                return redirect(url_for('details.get_details',posts=grandparent,page=1))
            else:
                return redirect(url_for('details.get_details',posts=parent,page=1))

        else:
            flash('您还没登录')
            return redirect(url_for('user.login'))
    if not current_user.is_authenticated:
        flash('您还没登录 请登录后发表')
    return render_template('posts/discuss.html',form=form,course=c,course1=c1,course2=c2)
