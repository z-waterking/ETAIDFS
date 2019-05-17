from Main import *
from functools import wraps
from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory
from model import *
from DBsession import *
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

#注册检验
def valid_register(username, email):
    dbsession = DatabaseManagement()
    query_filter = or_(User.username == username, User.email == email)
    user = dbsession.query_all(User, query_filter)
    if user:
        return False
    else:
        return True

#登录
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('email'):
            return func(*args, **kwargs)
        else:
            return redirect('login.html')
    return wrapper

#-------------------------注册------------------------------
@app.route('/register', methods=['POST','GET'])
def GetPage_register():
    return render_template('register.html')

@app.route('/RegisterEnter', methods=['POST','GET'])
def RegisterEnter():
    register_data = request.json
    print(register_data)
    #todo 校验注册信息是否重复，若不重复，则插入，返回正确，否则，返回重新注册
    # if request.method == 'POST':
    #     if request.form["password1"] != request.form["password2"]:
    #         flash('两次密码不一致，请重新输入！')
    #     elif valid_register(request.form["username"], request.form["email"]):
    #         user = User(username=request.form["username"], password=request.form["password1"], email=request.form["email"])
    #         dbsession1 = DatabaseManagement()
    #         dbsession1.add_obj(user)
    #         flash("成功注册！")
    #         return redirect(url_for("GetPage_login"))
    #     else:
    #         flash("该用户名或邮箱已被注册！")
    # return render_template('register.html')
    # user = User(username=)
    return json.dumps({'success': True})
#----------------------注册End------------------------------

#----------------------登录--------------------------------
@app.route('/login', methods=['POST', 'GET'])
def GetPage_login():
    #先替换为我自己的
    #登陆时得到前端的
        # if valid_login(request.form["email"], request.form["password"]):
        #     email = request.form["email"]
        #     flash('登录成功!')
        #     session['email'] = request.form["email"]
        #     return redirect(url_for("GetPage"))
        # else:
        #     flash('用户名或密码错误！')

    return render_template('login.html')

@app.route('/LoginEnter', methods=['POST', 'GET'])
def LoginEnter():
    data = request.json
    print(data)
    #todo 校验登陆
    return json.dumps({'success':True})
#-----------------------登陆End-------------------------------
