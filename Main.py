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
    return render_template('homepage_test_Total.html')

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


@app.route('/getdata',methods=['POST','GET'])
def GetData():
    data = request.json
    print('----')
    print(data)
    return json.dumps(data)

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)