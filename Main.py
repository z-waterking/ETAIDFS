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
def SaveJudgeResult():
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
@app.route('/GetTotalData',methods=['POST','GET'])
def GetTotalData():
    data = request.json
    print(data)
    #todo 根据前端请求查询对应的数据库
    #组织最后的数据
    result = {}
    result['success'] = True
    result['graph'] = 'line'
    result['title'] = '{} {}领域-{}总体趋势'.format(data['SecondaryClass'], data['ThirdClass'], data['ThirdDirectory'])
    # 如果是这个目录下的，则为散点图。否则为折线图。
    # 散点图不需要管stage的值。折线图需要管。
    if data['SecondDirectory'].strip() == '科学与技术发展关联聚类预测':
        result['xs'] = [200, 309, 421, 20, 402]
        result['ys'] = [110, 123, 130, 140, 150]
        result['graph'] = 'plot'
        result['label'] = ['Develop', 'Initial', 'Growup', 'Expand', 'Mature']
    else:
        result['xs'] = [2008, 2009, 2010, 2011, 2012]
        result['ys'] = [23, 34, 56, 29, 56]
        result['graph'] = 'line'
        result['stage'] = ['Develop', 'Initial', 'Growup', 'Expand', 'Mature']
    return json.dumps(result)

@app.route('/GetCountryData',methods=['POST','GET'])
def GetCountryData():
    data = request.json
    #{'FirstDirectory': '3D打印技术监测', 'SecondDirectory': '科学发展与产业化阶段关联趋势', 'ThirdDirectory': '科学热度与产业化阶段关联趋势', 'ForthDirectory': '国家分析', 'SecondaryClass': 'B', 'ThirdClass': '小类2', 'Country': 'US'}
    print(data)
    #todo 根据前端请求查询对应的数据库

    #组织对应的数据
    result = {}
    result['success'] = True
    result['graph'] = 'line'
    result['title'] = '{} {}领域-{}趋势-{}'.format(data['SecondaryClass'], data['ThirdClass'], data['ThirdDirectory'], data['Country'])
    # 如果是这个目录下的，则为散点图。否则为折线图。
    # 散点图不需要管stage的值。折线图需要管。
    if data['SecondDirectory'].strip() == '科学与技术发展关联聚类预测':
        result['xs'] = [200, 309, 421, 20, 402]
        result['ys'] = [110, 123, 130, 140, 150]
        result['graph'] = 'plot'
        result['label'] = ['Develop', 'Initial', 'Growup', 'Expand', 'Mature']
    else:
        result['xs'] = [2008, 2009, 2010, 2011, 2012]
        result['ys'] = [110, 123, 130, 140, 150]
        result['graph'] = 'line'
        result['stage'] = ['Develop', 'Initial', 'Growup', 'Expand', 'Mature']
    return json.dumps(result)
#-----------获取图表展示数据End---------------

@app.route('/Get',methods=['POST','GET'])
def Get():
    data = request.json
    print('----')
    print(data)
    return json.dumps(data)

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)