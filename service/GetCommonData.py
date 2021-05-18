from service.Main import *
from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory
from service.Main import app
from service.model import *
from service.DBsession import *

#-----------系统简介--------------------------------
@app.route('/GetIntroduction', methods=['POST','GET'])
def SysIntroduction():
    FirstDirectory = request.args.get("FirstDirectory")
    result = sysIntroduction(FirstDirectory)
    return json.dumps({'introduction': result})
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
    # print('GETIT')
    FirstDirectory = request.args.get("FirstDirectory")
    # #获取该大类对应的小类
    # CommonTotalThirdClass = []
    # Commonsecondaryclass = CommonSecondaryClass(FirstDirectory)
    # for classes in Commonsecondaryclass:
    #     CommonThirdClass = FindThirdClassBySecondaryClass(classes)
    #     for ThirdClass in CommonThirdClass:
    #         CommonTotalThirdClass.append(ThirdClass)
    # # return json.dumps(CommonTotalThirdClass[:2])
    # print(CommonTotalThirdClass)
    if FirstDirectory == '3D打印技术监测':
        result = ['CNTs Characterization Technology', 'CNTs Preparation Technology', 'CNTs Purification Technology',
                  'CNTs Modification Technology', 'CNTs Performance and Application',
                  'Graphene Characterization Technology', 'Graphene Preparation Technology',
                  'Graphene Purification Technology', 'Graphene Modification Technology', 'Graphene Performance and Application']
    elif FirstDirectory == '碳纳米管与石墨烯监测':
        result = ['Curing Technology', 'Sintering Technology', 'Spray Bonding Technology', 'Wire Melt Bonding Technology',
         'silk melt bonding technology', 'Powder or Granular Melt Bonding Technology', 'energy deposition Technology',
         'Powder Bed Fusion Deposition Technology', 'Plate Laminated Technology', 'vat photopolymerization',
         '3D Bioprinting', '3D Food Printing']
    else:
        result = ['speech recognition', 'human body static character recognition', 'human body activity character recognition', 'affective recognition', 'content and scene recognition', 'character recognition', 'spatial recognition', 'cognitive science and virtual reality', 'natural language processing ', 'machine learning', 'neural network', 'control and decision', 'intelligent learning', 'inference', 'computing and algorithm', 'framework and platform', 'Others', 'intelligent driving', 'big data acquisition', 'big data pretreatment', 'distributed file system and database', 'access interface and query language', 'big data computing model and system', 'big data analysis and mining', 'big data visualization', 'big data privacy and security', 'big data application', 'cloud computing']
    # a = ['CNTs Characterization Technology', 'CNTs Preparation Technology']
    # return json.dumps(['CNTs Characterization Technology', 'CNTs Preparation Technology'])
    return json.dumps(result)

#获取专家的生日
@app.route('/GetExpertBirthYear',methods=['POST','GET'])
def GetExpertBirthday():
    #TODO
    print('Get GetExpertBirthYear')
    CommonYears = []
    for i in range(1920, 2018):
        CommonYears.append(i)
    return json.dumps(CommonYears)
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
    GrantYears = []
    for i in range(1950, 2019):
        GrantYears.append(i)
    return json.dumps(GrantYears)
#获取授予月
@app.route('/GetGrantMonth',methods=['POST','GET'])
def GetGrantMonth():
    #TODO
    print('GetGrantMonth')
    GrantMonths = []
    for i in range(1, 13):
        GrantMonths.append(i)
    return json.dumps(GrantMonths)
#获取授予日
@app.route('/GetGrantDay',methods=['POST','GET'])
def GetGrantDay():
    #TODO
    print('GetGrantDay')
    GrantDays = []
    for i in range(1, 32):
        GrantDays.append(i)
    return json.dumps(GrantDays)
#-----------获取通用数据End---------------