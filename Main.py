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

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)

