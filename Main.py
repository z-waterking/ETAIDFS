from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify
import DBsession
from sqlalchemy import create_engine, and_, update, or_
from model import *
from Form import Login_Form, Register_Form
from flask_login import LoginManager,login_user,UserMixin,login_required

app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:catherine@127.0.0.1:1433/data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'catherine'

# @app.route('/index',methods=['POST','GET'])
# def GetPage():
#     return render_template('index.html')

@app.route('/new_page',methods=['POST','GET'])
def GetNewPage():
    A = request.args.get("a")
    B = request.args.get("b")
    print("--------------GETNEWPAGE-------------")
    print(A)
    print(B)
    return render_template('NewPage.html', data={"result":"OK"})

@app.route('/post_data',methods=['POST','GET'])
def PostData():
    data = request.json
    print("-------------POST-----------")
    print(data)
    return json.dumps({"result":"完成测试"})

@app.route('/get_data',methods=['POST','GET'])
def Data():
    A = request.args.get("a")
    B = request.args.get("b")
    print("--------------GET-------------")
    print(A)
    print(B)
    return json.dumps({"result":"完成测试"})

@app.route('/')
def index():
    form = Login_Form()
    return render_template('login.html', form=form)

@app.route('/login',methods=['GOT','POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        dbsession = DBsession.DatabaseManagement()
        query_filter = and_(username = form.username.data)
        user = dbsession.query_all(User, query_filter)
        if user is not None and user.password==form.password.data:
            login_user(user)
            flash('登陆成功')
            return render_template('')
        else:
            flash('用户名或密码错误')
            return render_template('login.html',form = form)

@app.route('/register',methods=['GOT','POST'])
def register():
    form = Register_Form()
    if request.method == 'Get':
        return render_template('register.html',form = form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if form.password.data == form.repassword.data:
                user = User(username=form.username.data, password=form.password.data)
                dbsession = DBsession.DatabaseManagement()
                dbsession.add_obj(user)
                flash(message = '注册成功')
                return redirect('/login')
            else:
                flash(message='两次输入密码不一致，请重新输入！')
                return render_template('/register.html',form=form)
        else:
            return 'None'

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)

