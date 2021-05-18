from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory
from service.module import *
import os,time,decimal
from werkzeug.utils import secure_filename
from flask_admin import Admin
app = Flask(__name__)

app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:catherine@127.0.0.1:1433/EmergingTechnologyForecastDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'catherine'
app.config["SQLALCHEMY_ECHO"] = True
#上传文件存放位置
UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['txt','pdf','doc','docx','png','jpg','gif','xls','xlsx','pptx','ppt','zip'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
admin = Admin(app)

#上传文件需要函数
def allowed_file(filename):
    return '.'in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

#注册校验--用户名存在
def valid_register1(username):
    dbsession = DatabaseManagement()
    query_filter = and_(User.username == username)
    user = dbsession.query_all(User, query_filter)
    if user:
        return True
    else:
        return False

#注册校验--邮箱存在
def valid_register2(email):
    dbsession = DatabaseManagement()
    query_filter = and_(User.email == email)
    user = dbsession.query_all(User, query_filter)
    if user:
        return True
    else:
        return False

#打开新链接的模版
@app.route('/new_page', methods=['POST', 'GET'])
def GetNewPage():
    A = request.args.get("a")
    B = request.args.get("b")
    print("--------------GETNEWPAGE-------------")
    print(A)
    print(B)
    return render_template('NewPage.html', data={"result":"OK"})

#页面测试
@app.route('/normal', methods=['POST', 'GET'])
def GetNormal():
    return render_template('homepage_normalUser.html')

@app.route('/expert', methods=['POST', 'GET'])
def GetExpert():
    return render_template('homepage_Expert.html')

@app.route('/admin', methods=['POST', 'GET'])
def GetAdmin():
    return render_template('homepage_Administrator.html')
#页面测试END


#-------------------------注册------------------------------
@app.route('/register', methods=['POST','GET'])
def GetPage_register():
    return render_template('register.html')

@app.route('/RegisterEnter', methods=['POST','GET'])
def RegisterEnter():
    register_data = request.json
    #开始检验注册的数据
    result = {'success': True, 'msg': '注册成功'}
    #如果用户名存在失败
    if valid_register1(register_data['username']):
        result['success'] = False
        result['msg'] = '用户名存在'
        return json.dumps(result)
    #如果邮箱存在失败
    elif valid_register2(register_data['email']):
        result['success'] = False
        result['msg'] = '邮箱存在'
        return json.dumps(result)
    else:
        #如果都不存在，则添加用户到数据库
        #iden均为1
        user = User(username=register_data["username"], password=register_data["password"], email=register_data["email"], iden=1)
        dbsession = DatabaseManagement()
        dbsession.add_obj(user)
        return json.dumps(result)
#----------------------注册End------------------------------

#----------------------登录--------------------------------
@app.route('/login', methods=['POST', 'GET'])
def GetPage_login():
    return render_template('login.html')

@app.route('/LoginEnter', methods=['POST', 'GET'])
def LoginEnter():
    Login_data = request.json
    #登录数据
    print(Login_data)
    result = {'success': True, 'msg': '登陆成功', 'email': '邮箱', 'iden': '1'}
    #todo 校验登陆
    #如果登录成功
    dbsession = DatabaseManagement()
    query_filter = and_(User.email == Login_data['email'], User.password == Login_data['password'])
    user = dbsession.query_all(User, query_filter)
    if user:
        for i in user:
            result['iden'] = i.iden
        result['email'] = Login_data['email']
        print(result)
        return json.dumps(result)
    else:
        result['msg'] = '用户名或密码错误，请重新输入！'
        return json.dumps(result)
#-----------------------登陆End-------------------------------

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    from service.LoginAndRegister import *
    from service.ExpertJudge_InformationManager import *
    from service.GetCommonData import *
    from service.ShowGraphData import *
    from service.UploadFile import *
    app.run(debug=True)
