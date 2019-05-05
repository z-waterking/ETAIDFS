from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session
from DBsession import *
from sqlalchemy import create_engine, and_, update, or_
from model import *
from functools import wraps

app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:catherine@127.0.0.1:1433/data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'catherine'


#辅助函数
#登录检验
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
    query_filter = and_(User.username == username, User.email == email)
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

@app.route('/index',methods=['POST','GET'])
def GetPage():
    return render_template('homepage.html')

@app.route('/index2',methods=['POST','GET'])
def GetPage2():
    return render_template('homepage_test_Total.html')

@app.route('/new_page', methods=['POST', 'GET'])
def GetNewPage():
    A = request.args.get("a")
    B = request.args.get("b")
    print("--------------GETNEWPAGE-------------")
    print(A)
    print(B)
    return render_template('NewPage.html', data={"result":"OK"})

@app.route('/newpage_index', methods=['POST','GET'])
@login_required
def GetNewPage_index():
    return render_template('index.html')

@app.route('/ExpertInformationManage',methods=['POST','GET'])
@login_required
def GetPage_ExpertInformationManage():
    return render_template('ExpertInformationManage.html')

# @app.route('/register',methods=['GET','POST'])
# def regist():

@app.route('/login', methods=['POST', 'GET'])
def GetPage_login():
    if request.method == 'POST':
        if valid_login(request.form["email"], request.form["password"]):
            email = request.form["email"]
            flash('登录成功!', category='warning')
            session['email'] = request.form["email"]
            return redirect(url_for("GetNewPage_index", useremail=email))
        else:
            flash('用户名或密码错误！')

#-----------专家提交数据------------
@app.route('/JudgeResult',methods=['POST','GET'])
def SaveJudgeRecult():
    data = request.json
    #TODO:Save data to database and return if it's success
    print(data)
    '''
    {'SecondaryClass': '请选择大类', 'ThirdClass': '请选择小类', 'DevelopStage': {'start': '起始年份', 'stop': '起始年份'}, 'InitialStage': {'start': '起始年份', 'stop': '起始年份'}, 'GrowupStage': {'start': '起始年份', 'stop': '起始年份'}, 'ExpandStage': {'start': '起始年份', 'stop': '起始年份'}, 'MatureStart': {'start': '起始年份', 'stop': '起始年份'}}
    '''
    result = {}
    result['success'] = True
    return json.dumps(result)
#-----------专家提交数据End---------------

#-----------获取通用数据------------------
#获取通用的国家
@app.route('/GetCommonCountrys',methods=['POST','GET'])
def GetCommonCountrys():
    CommonCountrys = ['US', 'UK', 'China']
    return json.dumps(CommonCountrys)

#获取通用的年份
@app.route('/GetCommonYear',methods=['POST','GET'])
def GetCommonYear():
    CommonYears = [2008, 2009, 2010]
    return json.dumps(CommonYears)

#直接获取大类
@app.route('/GetCommonSecondaryClass',methods=['POST','GET'])
def GetCommonSecondaryClass():
    CommonSecondaryClass = ['A', 'B', 'C']
    return json.dumps(CommonSecondaryClass)

#通过大类获取小类
@app.route('/GetCommonThirdClass',methods=['POST','GET'])
def GetCommonThirdClass():
    def FindThirdClassBySecondaryClass(SecondaryClass):
        return ['小类1', '小类2']
    SecondaryClass = request.args.get("SecondaryClass")
    CommonThirdClass = FindThirdClassBySecondaryClass(SecondaryClass)
    return json.dumps(CommonThirdClass)

#-----------获取通用数据End---------------

#-----------获取图表展示数据--------------

#-----------获取图表展示数据End---------------


    # return render_template('login.html')
@app.route('/register', methods=['POST','GET'])
def GetPage_register():
    if request.method == 'POST':
        if request.form["password1"] != request.form["password2"]:
            flash('两次密码不一致，请重新输入！')
        elif valid_register(request.form["username"], request.form["email"]):
            user = User(username=request.form["username"], password=request.form["password1"], email=request.form["email"])
            dbsession = DatabaseManagement()
            dbsession.add_obj(user)
            flash("成功注册！")
            return redirect(url_for("GetPage_login"))
        else:
            flash("该用户名或邮箱已被注册！")
    return render_template('/register.html')
@app.route('/getdata',methods=['POST','GET'])
def GetData():
    data = request.json
    print('----')
    print(data)
    return json.dumps(data)

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)