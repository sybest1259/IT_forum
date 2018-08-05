from flask import Blueprint,current_app
from App.extensions import db
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Seralize

test = Blueprint('test',__name__)

@test.route('/h/')
def hash_set():
    # password_hash = generate_password_hash('123456')
    # print('校验结果:',check_password_hash(password_hash,'555'))
    s = Seralize(current_app.config['SECRET_KEY'])
    return 'token：{}'.format(s.dumps({'id':1}))
    # return 'test'

