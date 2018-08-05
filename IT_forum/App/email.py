from flask import Flask,render_template,current_app
import os,time
from flask_mail import Mail,Message
from threading import Thread#导入线程模块
from App.extensions import mail

def send_message_async(app,msg):
    with app.app_context():#管理程序上下文
        mail.send(message=msg)


def send_message(subject,to,**kwargs):
    app = current_app._get_current_object()
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])
    msg.html = render_template('email/activate.html',**kwargs)
    t = Thread(target=send_message_async,args=(app,msg))
    t.start()#开启线程,异步响应用户操作，用户无需等待发送成功后才能进行下一步操作
    # time.sleep(2)
    # return '已发送'
def send_modify(subject,to,**kwargs):
    app = current_app._get_current_object()
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])
    msg.html = render_template('email/modify.html',**kwargs)
    t = Thread(target=send_message_async,args=(app,msg))
    t.start()#开启线程,异步响应用户操作，用户无需等待发送成功后才能进行下一步操作
    # time.sleep(2)
    # return '已发送'
def send_modify_activate(subject, to, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject=subject, recipients=[to], sender=app.config['MAIL_USERNAME'])
    msg.html = render_template('email/modify_activate.html', **kwargs)
    t = Thread(target=send_message_async, args=(app, msg))
    t.start()  # 开启线程,异步响应用户操作，用户无需等待发送成功后才能进行下一步操作
    # time.sleep(2)
    # return '已发送'


