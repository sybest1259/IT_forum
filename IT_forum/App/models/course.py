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

class Course(db.Model,Base):
    __tablename__ = 'course'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(23),index=True)
    abstract = db.Column(db.Text)
    pid = db.Column(db.Integer,default=0)
    path = db.Column(db.Text,default='0,')
    timestamp = db.Column(db.DateTime,default=datetime.utcnow())






