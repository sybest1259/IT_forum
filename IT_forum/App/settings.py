import os
#获取本语句所在py文件的绝对路径
BASE_PATH = os.path.abspath(os.path.dirname(__file__))#/home/songyu/PycharmProjects/untitled/blog/MVT/App
class Config():
    BOOTSTRAP_SERVE_LOCAL = True
    SECRET_KEY = '123'
    SQLALCHEMY_TRACK_MODIFICATIONS = False#如果设置成True(默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。如果你不显示的调用它，在最新版的运行环境下，会显示警告。
    # SQLALCHEMY_COMMIT_ROLLBACK = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True#数据库自动提交
    MAX_CONTENT_LENGTH = 1024 * 1024 * 5
    # UPLOADED_IMAGE_DEST = os.path.join(os.getcwd(), 'App/static/upload')
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_PATH,'static/upload')
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '604508260@qq.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 's7928661')
    EVERY_PAGE_NUM = 5
class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'+os.path.join(BASE_PATH,'dev-blog.sqlite')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:s89681114@127.0.0.1:3306/dev_blog'
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:s89681114@127.0.0.1:3306/test_blog'
    DEBUG = False
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:s89681114@127.0.0.1:3306/blog'
    DEBUG = False

class Default(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:s89681114@127.0.0.1:3306/blog'
    DEBUG = True

configDict = {'default':Default,'development':DevelopmentConfig,'testing':TestingConfig,'production':ProductionConfig}