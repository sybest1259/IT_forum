from flask import Blueprint,render_template,current_app,flash,request
from App.forms import UploadPhotos,UploadInfo,SubmitInfo
from App.extensions import file
from App.extensions import db
from App.models import User
from PIL import Image
from flask_login import current_user,login_required
import os,string,random
center = Blueprint('center',__name__)

def random_name(suffix,length=8):
    Str = string.ascii_letters+string.digits
    return ''.join(random.choice(Str) for i in range(length))+'.'+suffix
def img_zoom(path,width=200,height=200,prefix='s_'):
    img = Image.open(path)
    img.thumbnail((width, height))  # 重新设计尺寸
    img.save(path)  # 保存图片 覆盖掉原来的图片

@center.route('/center/',methods=['GET','POST'])
@login_required
def upload():
    form = UploadPhotos()
    form1 = UploadInfo()
    # form2 = SubmitInfo()
    if form.validate_on_submit():

        print(1111111111111111111111111111111111)
        photo = form.photo.data
        suffix = photo.filename.split('.')[-1]
        while True:
            newname = random_name(suffix)
            path = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],newname)
            if not os.path.exists(path):
                break
        file.save(photo,name=newname)
        if current_user.icon != 'default.jpg':
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],current_user.icon))
        img_zoom(path)
        current_user.icon = newname
        db.session.add(current_user)
        db.session.commit()
        img_url = file.url(current_user.icon)
        # print(img_url)
        flash('上传成功')
        # return render_template('owncenter/center.html', form=form,form1=form1,img_url=img_url)
    # if current_user.icon != 'default.jpg':
    img_url = file.url(current_user.icon)
    # else:
    #     img_url = '#'
    u1 = User.query.filter_by(username=current_user.username).first()
    if form1.validate_on_submit():
        if form1.sex.data == 'm':
            u1.sex = True
            u1.save()
        else:
            u1.sex = False
            u1.save()
        if form1.age.data != None:
            u1.age = form1.age.data
            u1.save()
            flash('修改成功')

    # if form1.sex.data == None:
    #     print(form1.sex.data)
    #     form1.sex.data = 'm'


    if u1.sex == True:
        form1.sex.data = 'm'
    else:
        form1.sex.data = 'w'
    form1.age.data = u1.age



    return render_template('owncenter/center.html',form=form,form1=form1,img_url=img_url)