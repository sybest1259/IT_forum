from App.extensions import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask import current_app
#生成token值 加密令牌 确定是谁访问
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize
from App.extensions import login_manager
from datetime import datetime,timedelta
#flask_login为 Flask 提供了用户会话管理。它处理了日常的登入，登出并且长时间记住用户的会话。
from flask_login import UserMixin
from .posts import Posts

class Base():
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()

class User(UserMixin,Base,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(15),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    sex = db.Column(db.Boolean,default=True)
    age = db.Column(db.Integer,default=20)
    email = db.Column(db.String(50))
    icon = db.Column(db.String(40),default='default.jpg')
    confirm = db.Column(db.Boolean,default=False)
    register_date = db.Column(db.DateTime,default=None)
    lastlogin_date = db.Column(db.DateTime,default=None)
    lastlogin_date_cache = db.Column(db.DateTime, default=None)
    #posts
    #参数一：引用关系模型
    #参数二：backref：反向引用的字段 给posts模型添加了一个user属性
    #       这个属性是替换uid进行查询的，uid用不上
    #参数三：加载数据条目(如何加载)，dynamic表示不添加，返回query对象，也就是sql语句
    #       默认值为：select，返回一个装有所有帖子对象的列表，不能通过过滤筛选或者其他操作
    #帖子名.user返回用户名

    #通过设置backref='user'，同时Posts表增加uid外键字段关联user表的id，使Posts.user.字段名可以访问user表的字段
    #例如：Posts.user返回<user 1>这种格式的数据
    posts = db.relationship('Posts',backref='user',lazy='dynamic')

    #db.backref:帖子被收藏的用户也是多的关系
    #secondary设置中间表
    #设置backref=db.backref('users',lazy='dynamic')，通过Posts.user查找收藏该帖子的所有用户，
    # 使用db.backref('users',lazy='dynamic')是因为Posts.user返回多条数据，需要设置dynamic使返回值为sql语句(posts字段返回一条数据所以不需要)
    #例如Posts.users返回sql查询语句，for i in Posts.users,i返回<user 1><user 2>...
    favorite = db.relationship('Posts',secondary='collections',backref=db.backref('users',lazy='dynamic'),lazy='dynamic')
    #外层dynamic为user.favorite(type类型为：<class 'sqlalchemy.orm.dynamic.AppenderBaseQuery'>)服务，db.backref中的dynamic为posts.users服务
    #使用user.favorite.append(Posts.query.get(id))和user.favorite.remove(Posts.query.get(id))更新该字段

    @property
    def password(self):
        raise AttributeError('密码不可读')
    #将明文密码变成哈希加密，再赋值给password_hash字段
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    # 验证密码
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    #生成token 通过邮件发送token值 进行账户激活
    def generate_token(self):
        s = Seralize(current_app.config['SECRET_KEY'])
        return s.dumps({'id': self.id})#将
    #测试token是否正确
    @staticmethod
    def check_token(token):
        s = Seralize(current_app.config['SECRET_KEY'])
        try:
            Dict = s.loads(token)#加载注册时传来的token字典
            id = Dict['id']#拿到用户id
            u = User.query.get(id)#查询id对象是否存在
            if not u:
                raise ValueError
        except:#token过期不正确
            return False
        #判断账户是否未激活 没有则激活，激活了则返回True
        if not u.confirm:
            u.confirm = True
            u.save()
        return True
    def return_token(token):
        s = Seralize(current_app.config['SECRET_KEY'])
        try:
            Dict = s.loads(token)#加载注册时传来的token字典
            id = Dict['id']#拿到用户id
            u = User.query.get(id)#查询id对象是否存在
            if not u:
                raise ValueError
        except:#token过期不正确
            return False
        return u
    #判断是否收藏
    def is_favorite(self,pid):
        data = self.favorite.all()
        # for p in data:
        #     if p.id == pid:
        #         return True
        if list(filter(lambda p:p.id==pid,data)):
            return True
        return False

    def add_favorite(self,pid):
        self.favorite.append(Posts.query.get(pid))

    def remove_favorite(self,pid):
        self.favorite.remove(Posts.query.get(pid))


#通过用户id不断重新加载用户对象，实时更新用户状态
@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)