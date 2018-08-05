from flask import Flask
from .settings import configDict#配置字典
from .extensions import config_extensions,file#第三方扩展库加载
from .views import blue_register#注册蓝本
from App.extensions import file

def create_app(configname):
    app = Flask(__name__)
    app.config.from_object(configDict[configname])
    config_extensions(app)
    blue_register(app)#注册蓝本
    return app