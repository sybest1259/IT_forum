from .main import main
from .user import user
from .test import test
from .owncenter import center
from .posts import posts
from .details import details
from .course import course
blueprint_config = [(main,'main/'),(user,'user/'),(test,'test/'),(center,'center/'),(posts,'posts/'),(details,'details/'),(course,'course/')]
def blue_register(app):
    for blue,prefix in blueprint_config:
        app.register_blueprint(blue,prefix=prefix)