from flask import jsonify,Blueprint,request,render_template,redirect,url_for,flash,current_app
from App.forms import SendPosts
from App.models import Posts,Course
from flask_login import current_user
from datetime import datetime,timedelta
from App.extensions import cache
from sqlalchemy import and_,not_

from sqlalchemy import and_
posts = Blueprint('posts',__name__)
@posts.route('/post/',methods=['GET','POST'])
def send_posts():
    form = SendPosts()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            p = Posts(title=form.articletitle.data,article=form.article.data,user=current_user,timestamp=datetime.utcnow()+timedelta(hours=8))
            print(p.timestamp)
            p.save()
            flash('发表成功')
            cache.clear()#因为数据库更新,页面也需要更新，所以需要清除所有缓存
            return redirect(url_for('posts.send_posts'))
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
    return render_template('posts/send_posts.html',form=form,course=c,course1=c1,course2=c2)
@posts.route('/show/',methods=['GET','POST'])
def show():
    from App.models import User
    p = Posts.query.get(1)
    print(p.user.username)
    u = User.query.get(1)#返回sql语句
    print(u.posts)#当前用户的所有帖子

    return ''
@posts.route('/search/index/',methods=['GET','POST'])
def index():
    if request.form.get('search'):
        keyword = request.form.get('search')
    else:
        keyword = 'python'
    return redirect(url_for('posts.search',key=keyword))
@posts.route('/search/<key>',methods=['GET','POST'])
def search(key):
    # print(11111111111111111111111111111111111111111111111)
    try:
        page = int(request.args.get('page',1))
    except:
        page = 1
    keyword = key
    print(keyword)
    keyword = key
    pagination = Posts.query.filter(Posts.title.contains(keyword),Posts.pid==0).paginate(page,current_app.config['EVERY_PAGE_NUM'],False)
    data = pagination.items
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('posts/search.html',data=data,pagination=pagination,keyword=keyword,course=c,course1=c1,course2=c2)
@posts.route('/collections/<int:pid>/')
def collections(pid):
    try:
        if current_user.is_favorite(pid):
            current_user.remove_favorite(pid)
        else:
            current_user.add_favorite(pid)
        return jsonify({'res':200})
    except:
        return jsonify({'res':401})
