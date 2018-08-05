from App.extensions import  db
from datetime import datetime,timedelta
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



"""
id
title
article
pid
path
time
dianzan

"""

class Posts(db.Model,Base):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(23),index=True)
    article = db.Column(db.Text)
    pid = db.Column(db.Integer,default=0)
    path = db.Column(db.Text,default='0,')
    fabulous = db.Column(db.Integer,default=0)
    times = db.Column(db.Integer,default=0)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow())
    scan = db.Column(db.Integer,default=0)
    #外键，与user表主键id关联，进行关联查询
    #表迁移后 表中会有一个uid字段 一对多 一个用户发表多个帖子
    uid = db.Column(db.Integer,db.ForeignKey('user.id'))




