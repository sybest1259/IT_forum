from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet,configure_uploads,patch_request_class,IMAGES
from flask_mail import Mail
from flask_login import LoginManager
from flask_moment import Moment
from flask_cache import Cache
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()
login_manager = LoginManager()
file = UploadSet('photos',IMAGES)
moment =Moment()
cache = Cache(config={'CACHE_TYPE':'simple'})#缓存类型simple(内存)
# cache = Cache(config={'CACHE_TYPE':'redis'})#缓存类型redis(redis数据库)


def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    cache.init_app(app)
    configure_uploads(app,file)
    patch_request_class(app, size=None)

    login_manager.init_app(app)
    #指定登录端点
    login_manager.login_view = 'user.login'
    #提示信息
    login_manager.login_message = '您还没有登录 请登录再访问'
    #session设置保护级别，strong表示会记录客户端ip和user-agent信息，一旦有异常会退出
    login_manager.session_protection = 'strong'
