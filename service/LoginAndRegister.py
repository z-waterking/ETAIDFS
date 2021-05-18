from service.Main import *
from service.Main import app
from functools import wraps
from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory
from service.model import *
from service.DBsession import *
#辅助函数
#登录检验，登陆时需要检查其权限
def valid_login(email, password):
    dbsession = DatabaseManagement()
    query_filter = and_(User.email == email, User.password == password)
    user = dbsession.query_all(User, query_filter)
    if user:
        return True
    else:
        return False

#登录
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('email'):
            return func(*args, **kwargs)
        else:
            return redirect('login.html')
    return wrapper

#取得自己的用户名、专家姓名