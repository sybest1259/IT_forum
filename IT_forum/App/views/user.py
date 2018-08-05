from flask import Blueprint,render_template,request,current_app,flash,get_flashed_messages,redirect,url_for
from App.models import User,Course
from App.forms import Register,file,Login,AgainActivate,Modify_code,Modify_email
from App.email import send_message,send_modify,send_modify_activate
from werkzeug.security import check_password_hash,generate_password_hash
import random,string,os,time
from PIL import Image
from datetime import datetime,timedelta
from sqlalchemy import and_,not_
#登录处理模块
from flask_login import login_user,login_required,logout_user,current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize
from App.extensions import cache
n = 0
user = Blueprint('user',__name__)

def random_name(suffix,length=8):
    Str = string.ascii_letters+string.digits
    return ''.join(random.choice(Str) for i in range(length))+'.'+suffix
def img_zoom(path,width=200,height=200,prefix='s_'):
    img = Image.open(path)
    img.thumbnail((width, height))  # 重新设计尺寸
    img.save(path)  # 保存图片 覆盖掉原来的图片
@user.route('/r/',methods=['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        # if request.method == 'POST' and request.files.get('uploadfile'):
        #     f1 = request.files.get('uploadfile')
        #     suffix = f1.filename.split('.')[-1]
        #     newname = random_name(suffix)
        #     path = os.path.join(current_app.config['UPLOADED_IMAGE_DEST'], newname)
        #     f1.save(path)
        #     img_url = file.url(filename=newname)
        #     img_zoom(path)

        u = User(username=form.username.data,password=form.userpass.data,email=form.email.data,register_date=datetime.utcnow()+timedelta(hours=8))
        u.save()
        token = u.generate_token()#token=s.dumps({'id': self.id})注册时先生成一个token通过id字段与当前用户绑定
        send_message('账户激活',u.email,username=u.username,token=token)#将token传递到激活函数activate()
        flash('注册成功，前往邮箱进行激活')
        # return '注册成功'


    #     return render_template('user/register.html',form=form,img_url=img_url)
    ######################################################
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('user/register.html', form=form,course=c,course1=c1,course2=c2)

@user.route('/test/')
def test():
    dataList = User.query.all()
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('user/show.html', data=dataList,course=c,course1=c1,course2=c2)
@user.route('/ia/')
def insert_all():
    u1 = User(username='li5',sex=False,age=19)
    u2 = User(username='li6',sex=False,age=20)
    User.save_all(u1,u2)
    return 'insert_all'
@user.route('/act/<token>')#点击邮件激活后访问该路由
def activate(token):
    #调用校验token的方法 激活成功或者失败
    if User.check_token(token):#如果传入的token解析出的用户id存在返回True，并将confirm值修改为1，不存在返回False
        flash('激活成功！请登录')
        return redirect(url_for('user.login'))
    else:
        flash('激活失败 请重新点击激活码 进行账户的激活')
        return redirect(url_for('user.register'))

@user.route('/l/',methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if not u:
            flash('当前用户不存在')
        elif not u.confirm:
            flash('你的账户未激活')
        elif u.check_password(form.userpass.data):
            flash('登录成功,欢迎'+u.username)
            login_user(u)#维护登录对象u
            cache.clear()
            u.lastlogin_date_cache = datetime.utcnow()+timedelta(hours=8)
            u.save()
            return redirect(url_for('main.index'))
        else:
            flash('请输入正确的密码')
        # return render_template('')
    #############################################
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('user/login.html',form=form,course=c,course1=c1,course2=c2)

@user.route('/lo/')
def logout():
    u = User.query.filter_by(username=current_user.username).first()
    u.lastlogin_date = u.lastlogin_date_cache
    u.save()
    logout_user()
    cache.clear()
    return redirect(url_for('main.show', page=1))

@user.route('/c/')
@login_required#设置登录才能访问的路由，没登录访问提示：login_manager.login_message的信息
def center():
    return '必须登录才能访问'

@user.route('/aa/',methods=['GET','POST'])
def again_activate():
    form = AgainActivate()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if not u:
            flash('激活用户不存在')
        elif u.confirm:
            flash('用户已激活')
        elif not u.check_password(form.userpass.data):
            flash('密码不正确')
        else:
            token = u.generate_token()
            send_message('请再次激活',u.email,username=u.username,token=token)
            flash('激活邮件已发送,请前往邮箱激活')
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('user/again_activate.html',form=form,course=c,course1=c1,course2=c2)
@user.route('/mc/',methods=['GET','POST'])
def modify_code():
    form = Modify_code()
    if form.validate_on_submit():
        u = User.query.filter_by(username=current_user.username).first()
        if u.check_password(form.userpass.data):
            u.password_hash = generate_password_hash(form.userpass1.data)
            u.save()
            flash('密码修改成功')
        else:
            flash('原始密码不正确')
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('user/modify_code.html',form=form,course=c,course1=c1,course2=c2)
@user.route('/cme/',methods=['GET','POST'])
def confirm_modify():
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('email/confirm_modify.html',course=c,course1=c1,course2=c2)
@user.route('/me/',methods=['GET','POST'])
def modify_email():
    u = User.query.filter_by(username=current_user.username).first()
    token = u.generate_token()
    send_modify('更改邮箱',u.email,token=token,username=u.username)
    flash('邮件已发送 请登录当前邮箱进行确认操作')
    return redirect(url_for('main.index'))

@user.route('/ne/<token>', methods=['GET', 'POST'])
def new_email(token):
    form = Modify_email()
    # u = User.query.filter_by(username=current_user.username).first()
    if User.return_token(token):
        u = User.return_token(token)
        if form.validate_on_submit():
            # s = Seralize(current_app.config['SECRET_KEY'])
            # Dict = s.loads(token)  # 加载注册时传来的token字典
            # id = Dict['id']  # 拿到用户id
            # print('id-------------',id)
            # print('confirm-------------', u.confirm)
            # u = User.query.get(id)  # 查询id对象是否存在

            email = form.email.data
            # u.save()

            send_modify_activate('请激活新邮箱', form.email.data, username=u.username, token=token,email=email)
            return '邮件已发送 请前往邮箱激活'#modify_activate.html
    c = Course.query.filter_by(pid=0)
    c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
    c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
    return render_template('user/modify_email.html', form=form,course=c,course1=c1,course2=c2)#modify_email.html
@user.route('/new/act/<token>/<email>')#点击邮件激活后访问该路由
def new_email_activate(token,email):
    #调用校验token的方法 激活成功或者失败
    if User.check_token(token):#如果传入的token解析出的用户id存在返回True，并将confirm值修改为1，不存在返回False
        u = User.return_token(token)
        u.email = email
        u.save()
        flash('新邮箱激活成功！请登录')
        return redirect(url_for('user.login'))
    else:
        flash('激活失败!请重新进行修改邮箱操作')
        c = Course.query.filter_by(pid=0)
        c1 = Course.query.filter(and_(Course.path.endswith(','), Course.pid != 0))
        c2 = Course.query.filter(and_(not_(Course.path.endswith(',')), Course.pid != 0))
        return render_template('main/index.html',course=c,course1=c1,course2=c2)