from flask import Blueprint,render_template,current_app,flash,request,redirect,url_for
from App.forms import UploadPhotos,UploadInfo,SubmitInfo
from App.extensions import file
from App.extensions import db
from App.models import User,Posts,Course
from PIL import Image
from datetime import datetime,timedelta
from flask_login import current_user,login_required
from sqlalchemy import and_,not_
import os,string,random

center = Blueprint('center',__name__)

def random_name(suffix,length=8):
    Str = string.ascii_letters+string.digits
    return ''.join(random.choice(Str) for i in range(length))+'.'+suffix
def img_zoom(path,width=200,height=200,prefix='s_'):
    img = Image.open(path)
    img.thumbnail((width, height))  # 重新设计尺寸
    pathSplit = os.path.split(path)
    newpath = os.path.join(pathSplit[0],prefix+pathSplit[1])#为压缩后的图片名加上前缀
    img.save(newpath)  # 保存图片
@center.route('/center/index/')
def index():
    return redirect(url_for('center.self_center',page=1))
@center.route('/center/<int:page>',methods=['GET','POST'])
@login_required
def self_center(page):
    form = UploadInfo()
    img_url = file.url(current_user.icon)
    u = User.query.filter_by(username=current_user.username).first()
    if form.validate_on_submit():
        if form.sex.data == 'm':
            u.sex = True
            u.save()
        else:
            u.sex = False
            u.save()
        if form.age.data != None:
            u.age = form.age.data
            u.save()
            flash('修改成功')
    if u.sex == True:
        form.sex.data = 'm'
    else:
        form.sex.data = 'w'
    form.age.data = u.age
    register_date = u.register_date
    lastlogin_date = u.lastlogin_date
    now = datetime.utcnow() + timedelta(hours=8)
    date = str((now-register_date)).split(' ')
    if len(date) == 1:
        date = 1
    else:
        date = int(date[0])
    print(now)
    print(register_date)
    print(date)
    print("--------------------------------")
    print(u.favorite)
    print("--------------------------------")
    print(User.query.filter_by(confirm=1))
    print(type(User.query.filter_by(confirm=1)))
    print(type(u.favorite))
    listp = []
    for post in u.favorite.all():
        listp.append(post.id)
    print(listp)
    pagination = Posts.query.filter(Posts.id.in_(listp)).paginate(page, current_app.config['EVERY_PAGE_NUM'], False)
    favorite = pagination.items
    #########################################
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('owncenter/center.html',form=form,img_url=img_url,date=date,lastlogin_date=lastlogin_date,now=now,pagination=pagination,favorite=favorite,course=c,course1=c1,course2=c2)
@center.route('/upload_icon/',methods=['GET','POST'])
@login_required
def upload_icon():
    form = UploadPhotos()
    if current_user.icon != 'default.jpg':
        img_url = file.url(current_user.icon.split('_')[1])
    else:
        img_url = file.url('default.jpg')
    if form.validate_on_submit():
        photo = form.photo.data
        suffix = photo.filename.split('.')[-1]
        while True:
            newname = random_name(suffix)
            path = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], newname)
            if not os.path.exists(path):
                break
        file.save(photo, name=newname)
        img = Image.open(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], newname))
        if 1.3 < img.size[1]/img.size[0] < 1.5:
            if current_user.icon != 'default.jpg':
                os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], current_user.icon))
                os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], current_user.icon.split('_')[1]))
            img_zoom(path)
            current_user.icon = 's_' + newname
            db.session.add(current_user)
            db.session.commit()
            img_url = file.url(current_user.icon.split('_')[1])
            # print(img_url)
            flash('上传成功')
        else:
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], newname))
            flash('图片尺寸比例必须为1.3-1.5')
    ############################################
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('owncenter/icon.html', form=form, img_url=img_url,course=c,course1=c1,course2=c2)