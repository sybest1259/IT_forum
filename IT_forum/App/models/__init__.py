from .user import User
from .posts import Posts
from .course import Course
from App.extensions import db

#收藏帖子表，user和posts共用的中间表，在init中创建
collections = db.Table('collections',db.Column('user_id',db.Integer,db.ForeignKey('user.id')),db.Column('posts_id',db.Integer,db.ForeignKey('posts.id')))