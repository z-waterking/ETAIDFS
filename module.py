from DBsession import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, and_, update, or_
from model import *
#-------------专家提交数据-------------
def saveJudgeResult(data):
    thirdClass = data['ThirdClass']
    #获取专家每个阶段判断年份，在数据库中标识年份对应阶段
    #获取developstage年份
    for i in ['DevelopStage','InitialStage','GrowupStage','ExpandStage','MatureStart']:
        developStart = data[i]['start']
        developEnd = data[i]['stop']
        dbsession = DatabaseManagement()
        query_filter = and_(ExpertJudge.Class == thirdClass, ExpertJudge.Year >= developStart, ExpertJudge.Year <= developEnd)
        expertJudge = dbsession.query_all(ExpertJudge, query_filter)
        for instance in expertJudge:
            instance.Stage == 'A'
    result = {}
    # return result
#-------------获取通用数据-------------
#获取通用的国家
def CommonCountrys():
    CommonCountrys = []
    dbsession = DatabaseManagement()
    query_filter = Country.ID >= 1
    country = dbsession.query_all(Country, query_filter)
    for data in country:
        CommonCountrys.append(data.Country)
    return CommonCountrys

#直接获取大类
def CommonSecondaryClass(Firstdirectory):
    CommonSecondaryClass = []
    dbsession = DatabaseManagement()
    if Firstdirectory == '3D打印技术监测':
        query_filter = and_(DictClas.Code.like('00_'),DictClas.Subsys == '002')
    elif Firstdirectory == '碳纳米管与石墨烯监测':
        query_filter = and_(DictClas.Code.like('00_'),DictClas.Subsys == '003')
    else:
        query_filter = and_(DictClas.Code.like('00_'),DictClas.Subsys == '001')
    secondaryclass = dbsession.query_all(DictClas, query_filter)
    for data in secondaryclass:
        CommonSecondaryClass.append(data.Class)
    return CommonSecondaryClass

#通过大类获取小类
def FindThirdClassBySecondaryClass(SecondaryClass):
    FindThirdClassBySecondaryClass = []
    dbsession = DatabaseManagement()
    query_filter = and_(DictClas.Class == SecondaryClass, DictClas.Code.like('00_'))
    secondaryclass = dbsession.query_all(DictClas, query_filter)
    for instance in secondaryclass:
        secondaryclasscode = instance.Code
        secondarySubclass = instance.Subsys
        print(secondaryclasscode)
    query_filter1 = and_(DictClas.Code.like('%s%%%%'%secondaryclasscode), DictClas.Code.like('00____'),DictClas.Subsys == secondarySubclass)
    findthirdclass = dbsession.query_all(DictClas, query_filter1)
    # findthirdclass = dbsession.execute_sql("select * from Dict_Class where Code like '%s%%%%'" % secondaryclasscode)
    for data in findthirdclass:
        FindThirdClassBySecondaryClass.append(data.Class)

    return FindThirdClassBySecondaryClass

#-----------获取图表展示数据--------------
def gettotalData(ThirdClass,ThirdDirectory,ForthDirectory):
    result = {}
    xs = []
    ys = []
    if ThirdDirectory == '科学热度与产业化阶段关联趋势':
        if ForthDirectory == '总体分析':
            #去表PaperHotDegree查
            dbsession = DatabaseManagement()
            query_filter = and_(PaperHotDegree._class == ThirdClass)
            data = dbsession.query_all(PaperHotDegree, query_filter)
            print(data)
            for instance in data:
                xs.append(instance['Hot_degree'])
                ys.append(instance['year'])

            return xs,ys
        else:
            #去表PaperCountryHotDegree查
            return result
    elif ThirdDirectory == '科学影响力与产业化阶段关联趋势':
        if ForthDirectory == '总体分析':
            # 去表PaperInfluence查
            return result
        else:
            # 去表PaperCountryInfluence查
            return result
    elif ThirdDirectory == '技术热度与产业化阶段关联趋势':
        if ForthDirectory == '总体分析':
            #去表PatentHotDegree查
            return result
        else:
            #去表PatentCountryHotDegree查
            return result
    elif ThirdDirectory == '技术影响力与产业化阶段关联趋势':
        if ForthDirectory == '总体分析':
            #去表PatentInfluence查
            return result
        else:
            #去表PatentCountryInfluence查
            return result