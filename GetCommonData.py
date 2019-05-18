from Main import *
from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory

from Main import app
from model import *
from DBsession import *

#-----------系统简介--------------------------------
@app.route('/GetIntroduction', methods=['POST','GET'])
def SysIntroduction():
    FirstDirectory = request.args.get("FirstDirectory")
    result = sysIntroduction(FirstDirectory)
    return json.dumps({'introduction':result})
#-----------系统简介end-----------------------------

#-----------获取通用数据------------------
#获取通用的国家
@app.route('/GetCommonCountrys', methods=['POST','GET'])
def GetCommonCountrys():
    Commoncountrys = CommonCountrys()
    return json.dumps(Commoncountrys)

#获取通用的年份
@app.route('/GetCommonYear',methods=['POST','GET'])
def GetCommonYear():
    CommonYears = []
    for i in range(2000, 2019):
        CommonYears.append(i)
    return json.dumps(CommonYears)

#直接获取大类
@app.route('/GetCommonSecondaryClass',methods=['POST','GET'])
def GetCommonSecondaryClass():
    Firstdirectory = request.args.get("FirstDirectory")
    print(Firstdirectory)
    Commonsecondaryclass = CommonSecondaryClass(Firstdirectory)
    return json.dumps(Commonsecondaryclass)
    ''' FirstDirectory'''
    # CommonSecondaryClass = ['A', 'B', 'C']
    return json.dumps(CommonSecondaryClass)

#通过大类获取小类
@app.route('/GetCommonThirdClass',methods=['POST','GET'])
def GetCommonThirdClass():
    # def FindThirdClassBySecondaryClass(SecondaryClass):
    #     return ['小类1', '小类2']
    ''' FirstDirectory'''
    SecondaryClass = request.args.get("SecondaryClass")
    CommonThirdClass = FindThirdClassBySecondaryClass(SecondaryClass)
    return json.dumps(CommonThirdClass)

#获取专家信息管理中的技术领域
@app.route('/GetExpertTecnology',methods=['POST','GET'])
def GetExpertTecnology():
    #TODO
    print('GETIT')
    FirstDirectory = request.args.get("FirstDirectory")
    #获取该大类对应的小类
    return json.dumps(['A','B','C'])
#获取专家的生日
@app.route('/GetExpertBirthYear',methods=['POST','GET'])
def GetExpertBirthday():
    #TODO
    print('Get GetExpertBirthYear')
    return json.dumps([2000, 2011, 2012])
#获取省市
@app.route('/GetExpertProvince',methods=['POST','GET'])
def GetExpertProvince():
    #TODO
    print('Get Province')
    return json.dumps(['北京市', '天津市', '上海市', '重庆市', '内蒙古自治区',
                       '辽宁省', '吉林省', '黑龙江省', '河北省', '江苏省',
                       '浙江省', '安徽省', '福建省', '江西省', '山东省',
                       '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区',
                       '海南省', '山西省', '四川省', '贵州省', '云南省',
                       '西藏自治区', '陕西省', '甘肃省', '青海省', '宁夏回族自治区',
                       '新疆维吾尔自治区', '香港', '澳门', '台湾'
                       ])
#获取GetHighestDegree
@app.route('/GetHighestDegree',methods=['POST','GET'])
def GetHighestDegree():
    #TODO
    print('Get Province')
    return json.dumps(['副学士学位', '学士学位', '硕士学位', '博士学位'])
#获取授予年
@app.route('/GetGrantYear',methods=['POST','GET'])
def GetGrantYear():
    #TODO
    print('GetGrantYear')
    return json.dumps([2000, 2001])
#获取授予月
@app.route('/GetGrantMonth',methods=['POST','GET'])
def GetGrantMonth():
    #TODO
    print('GetGrantMonth')
    return json.dumps([1, 2])
#获取授予日
@app.route('/GetGrantDay',methods=['POST','GET'])
def GetGrantDay():
    #TODO
    print('GetGrantDay')
    return json.dumps([1, 2, 3])

#-----------获取通用数据End---------------