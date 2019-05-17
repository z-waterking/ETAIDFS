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
