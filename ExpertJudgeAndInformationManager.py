from Main import *
from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory
from model import *
from DBsession import *

#-----------专家信息管理------------
@app.route('/SaveExpertInformation',methods = ['POST','GET'])
def ExpertManage():
    data = request.get_json(force=True)
    print('***', data)
    result = data
    if request.method == 'POST':
        expert = ExpertList(Expert_Name=data['Name'], Birth_Year=data['Birthday'], Sex=data['Sex'], People=data['Nation'],
                            Institution=data['WorkPlace'],Professional_Title=data['Title'], Administrative_duty=data['Job'],
                            City=data['City'], Province=data['Province'], Address=data['Address'], Zip=data['PostCode'],
                            Highestdegree=data['HighestDegree'], Degreedate=data['GrantTime'], University=data['GrantUniversity'],
                            Country=data['GrantCountry'], Honorary_Reward=data['HonorAndReward'], Tel=data['Phone'],
                            Email=data['Email'], Class=','.join(data['TechnicalField']))
        dbsession = DatabaseManagement()
        dbsession.add_obj(expert)
    result['success'] = True
    return json.dumps(result)
#-----------专家信息管理end------------

#-----------专家信息------------
@app.route('/GetExpertData',methods=['POST','GET'])
def GetExpertData():
    email = request.args.get('email')
    result = {}
    result['exist'] = False
    #todo 根据email查找专家的信息，存在的话，将标记置为存在，且返回。否则，不返回。
    dbsession = DatabaseManagement()
    query_filter = and_(ExpertList.Email == email)
    expert = dbsession.query_all(ExpertList, query_filter)


    #如果专家提交过信息
    if expert == []:
        pass
    else:
        #如果已填写，返回专家信息
        result['exist'] = True
        for i in expert:
            result['Name'] = i.Expert_Name
            result['Birthday'] = i.Birth_Year
            result['Sex'] = i.Sex
            result['Nation'] = i.People
            result['WorkPlace'] = i.Institution
            result['Title'] = i.Professional_Title
            result['Job'] = i.Administrative_duty
            result['City'] = i.City
            result['Province'] = i.Province
            result['Address'] = i.Address
            result['PostCode'] = i.Zip
            result['HighestDegree'] = i.Highestdegree
            #分解为年月日
            result['GrantTime'] = i.Degreedate
            result['GrantYear'] = result['GrantTime'][:result['GrantTime'].index('年')]
            result['GrantMonth'] = result['GrantTime'][result['GrantTime'].index('年')+1:result['GrantTime'].index('月')]
            result['GrantDay'] =result['GrantTime'][result['GrantTime'].index('月')+1:result['GrantTime'].index('日')]

            result['GrantUniversity'] = i.University
            result['GrantCountry'] = i.Country
            result['HonorAndReward'] = i.Honorary_Reward
            result['Phone'] = i.Tel
            result['Email'] = i.Email
            result['Class'] = i.Class.split(',')
            print(result)
    return json.dumps(result)

#-----------------------------------
#-----------专家提交数据------------
@app.route('/JudgeResult',methods=['POST','GET'])
def SaveJudgeResult():
    data = request.json
    #TODO:Save data to database and return if it's success
    print(data)
    '''
    {'SecondaryClass': '请选择大类', 'ThirdClass': '请选择小类', 'DevelopStage': {'start': '起始年份', 'stop': '起始年份'}, 'InitialStage': {'start': '起始年份', 'stop': '起始年份'}, 'GrowupStage': {'start': '起始年份', 'stop': '起始年份'}, 'ExpandStage': {'start': '起始年份', 'stop': '起始年份'}, 'MatureStart': {'start': '起始年份', 'stop': '起始年份'}}
    '''
    result = data
    saveJudgeResult(result)
    result['success'] = True
    return json.dumps(result)
#-----------专家提交数据End---------------
