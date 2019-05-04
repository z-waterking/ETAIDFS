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
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'catherine'

@app.route('/index',methods=['POST','GET'])
def GetPage():
    return render_template('homepage.html')

@app.route('/index2',methods=['POST','GET'])
def GetPage2():
    return render_template('homepage_test_GetPost.html')

@app.route('/new_page',methods=['POST','GET'])
def GetNewPage():
    A = request.args.get("a")
    B = request.args.get("b")
    print("--------------GETNEWPAGE-------------")
    print(A)
    print(B)
    return render_template('NewPage.html', data={"result":"OK"})

@app.route('/newpage_index',methods=['POST','GET'])
def GetNewPage_index():
    return render_template('index.html')

@app.route('/ExpertInformationManage',methods=['POST','GET'])
def GetPage_ExpertInformationManage():
    return render_template('ExpertInformationManage.html')

@app.route('/login',methods=['POST','GET'])
def GetPage_login():
    return render_template('login.html')

@app.route('/getdata',methods=['POST','GET'])
def GetData():
    data = request.json
    print('----')
    print(data)
    return json.dumps(data)

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)