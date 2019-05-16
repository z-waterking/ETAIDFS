from DBsession import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, and_, update, or_
from model import *
def sysIntroduction(FirstDirectory):
    dbsession = DatabaseManagement()
    query_filter = and_(SysIntroduction.title == FirstDirectory)
    sys_introduction = dbsession.query_all(SysIntroduction, query_filter)
    result = []
    for instance in sys_introduction:
        result.append(instance.abstract)
    return result[0]

#-------------专家提交数据-------------
def saveJudgeResult(data):
    thirdClass = data['ThirdClass']
    #获取专家每个阶段判断年份，在数据库中标识年份对应阶段
    #获取developstage年份
    for i in ['DevelopStage','InitialStage', 'GrowupStage', 'ExpandStage', 'MatureStart']:
        developStart = data[i]['start']
        developEnd = data[i]['stop']
        dbsession = DatabaseManagement()
        query_filter = and_(ExpertJudge.Class == thirdClass, ExpertJudge.Year >= developStart, ExpertJudge.Year <= developEnd)
        expertJudge = dbsession.query_all(ExpertJudge, query_filter)
        print(expertJudge)
        for instance in expertJudge:
            if i == 'DevelopStage':
                instance.Stage = 'A'
            elif i == 'InitialStage':
                instance.Stage = 'B'
            elif i == 'GrowupStage':
                instance.Stage = 'C'
            elif i == 'ExpandStage':
                instance.Stage = 'D'
            else:
                instance.Stage = 'E'

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
    xs = []
    ys = []
    if ThirdDirectory == '科学发展热度与产业发展阶段关联趋势':
        if ForthDirectory == '总体分析':
            #去表PaperHotDegree查
            dbsession = DatabaseManagement()
            query_filter = and_(PaperHotDegree._class == ThirdClass)
            data = dbsession.query_order_by(PaperHotDegree, query_filter, "year")
            # print(data)
            for instance in data:
                xs.append(instance.year)
                ys.append(instance.Hot_degree)
            return xs, ys
    elif ThirdDirectory == '科学发展影响力与产业发展关联趋势':
        if ForthDirectory == '总体分析':
            # 去表PaperInfluence查
            dbsession = DatabaseManagement()
            query_filter = and_(PaperInfluence._class == ThirdClass)
            data = dbsession.query_order_by(PaperInfluence, query_filter, "year")
            # print(data)
            for instance in data:
                xs.append(instance.year)
                ys.append(instance.Influence)
            return xs, ys
    elif ThirdDirectory == '技术发展热度与产业发展阶段关联趋势':
        if ForthDirectory == '总体分析':
            #去表PatentHotDegree查
            dbsession = DatabaseManagement()
            query_filter = and_(PatentHotDegree._class == ThirdClass)
            data = dbsession.query_order_by(PatentHotDegree, query_filter,"year")
            # print(data)
            for instance in data:
                xs.append(instance.year)
                ys.append(instance.Hot_degree)
            return xs, ys
    elif ThirdDirectory == '技术发展影响力与产业发展阶段关联趋势':
        if ForthDirectory == '总体分析':
            #去表PatentInfluence查
            dbsession = DatabaseManagement()
            query_filter = and_(PatentInfluence._class == ThirdClass)
            data = dbsession.query_order_by(PatentInfluence, query_filter, "year")
            # print(data)
            for instance in data:
                xs.append(instance.year)
                ys.append(instance.Influence)
            return xs, ys
    elif ThirdDirectory == '科学热度与技术热度关联聚类监测':
        if ForthDirectory == '总体分析':
            #去表PaperHotDegree和表PatentHotDegree查
            dbsession = DatabaseManagement()
            query_filter1 = and_(PatentHotDegree._class == ThirdClass)
            query_filter2 = and_(PaperHotDegree._class == ThirdClass)
            data1 = dbsession.query_order_by(PatentHotDegree, query_filter1, "year")
            data2 = dbsession.query_order_by(PaperHotDegree, query_filter2, "year")
            # print(data1)
            # print(data2)
            for instance in data1:
                #应该是热度
                ys.append(instance.Hot_degree)
            for instance in data2:
                #应该是热度
                xs.append(instance.Hot_degree)
            return xs, ys
    elif ThirdDirectory == '科学影响力与技术影响力聚类关联分析':
        if ForthDirectory == '总体分析':
            dbsession = DatabaseManagement()
            query_filter1 = and_(PatentInfluence._class == ThirdClass)
            query_filter2 = and_(PaperInfluence._class == ThirdClass)
            data1 = dbsession.query_order_by(PatentInfluence, query_filter1, "year")
            data2 = dbsession.query_order_by(PaperInfluence, query_filter2, "year")
            # print(data1)
            # print(data2)
            for instance in data1:
                # 应该是影响力
                ys.append(instance.Influence)
            for instance in data2:
                # 应该是影响力
                xs.append(instance.Influence)
            return xs, ys
def gettotalCountryData(ThirdClass,ThirdDirectory,ForthDirectory,Country):
    xs = []
    ys = []
    if ThirdDirectory == '科学发展热度与产业发展阶段关联趋势':
        if ForthDirectory == '国家分析':
            #去表PaperCountryHotDegree查
            dbsession = DatabaseManagement()
            query_filter = and_(PaperCountryHotDegree._class == ThirdClass,PaperCountryHotDegree.country == Country)
            data = dbsession.query_order_by(PaperCountryHotDegree, query_filter,"year")
            # print(data)
            for instance in data:
                xs.append(instance.year)
                ys.append(instance.Hot_degree)
            return xs, ys
    elif ThirdDirectory == '科学发展影响力与产业发展关联趋势':
        if ForthDirectory == '国家分析':
            # 去表PaperCountryInfluence查
            dbsession = DatabaseManagement()
            query_filter = and_(PaperCountryInfluence._class == ThirdClass,PaperCountryInfluence.country == Country)
            data = dbsession.query_order_by(PaperCountryInfluence, query_filter, "year")
            # print(data)
            for instance in data:
                xs.append(instance.year)
                ys.append(instance.Influence)
            return xs, ys
    elif ThirdDirectory == '技术发展热度与产业发展阶段关联趋势':
        if ForthDirectory == '国家分析':
            #去表PatentCountryHotDegree查
            dbsession = DatabaseManagement()
            query_filter = and_(PatentCountryHotDegree._class == ThirdClass, PatentCountryHotDegree.country == Country)
            data = dbsession.query_order_by(PatentCountryHotDegree, query_filter, "year")
            # print(data)
            for instance in data:
                xs.append(instance.year)
                ys.append(instance.Hot_degree)
            return xs, ys
    elif ThirdDirectory == '技术发展影响力与产业发展阶段关联趋势':
        if ForthDirectory == '国家分析':
            #去表PatentCountryInfluence查
            dbsession = DatabaseManagement()
            query_filter = and_(PatentCountryInfluence._class == ThirdClass, PatentCountryInfluence.country == Country)
            data = dbsession.query_order_by(PatentCountryInfluence, query_filter,"year")
            # print(data)
            for instance in data:
                xs.append(instance.year)
                ys.append(instance.Influence)
            return xs, ys
    elif ThirdDirectory == '科学热度与技术热度关联聚类监测':
        if ForthDirectory == '国家分析':
            #去表PaperHotDegree和表PatentHotDegree查
            dbsession = DatabaseManagement()
            query_filter1 = and_(PatentCountryHotDegree._class == ThirdClass, PatentCountryHotDegree.country == Country)
            query_filter2 = and_(PaperCountryHotDegree._class == ThirdClass, PaperCountryHotDegree.country == Country)
            data1 = dbsession.query_order_by(PatentCountryHotDegree, query_filter1,"year")
            data2 = dbsession.query_order_by(PaperCountryHotDegree, query_filter2, "year")
            # print(data1)
            # print(data2)
            for instance in data1:
                #应该是热度
                ys.append(instance.Hot_degree)
            for instance in data2:
                #应该是热度
                xs.append(instance.Hot_degree)
            return xs, ys
    elif ThirdDirectory == '科学影响力与技术影响力聚类关联分析':
        if ForthDirectory == '国家分析':
            dbsession = DatabaseManagement()
            query_filter1 = and_(PatentCountryInfluence._class == ThirdClass, PatentCountryInfluence.country == Country)
            query_filter2 = and_(PaperCountryInfluence._class == ThirdClass, PaperCountryInfluence.country == Country)
            data1 = dbsession.query_order_by(PatentCountryInfluence, query_filter1, "year")
            data2 = dbsession.query_order_by(PaperCountryInfluence, query_filter2, "year")
            # print(data1)
            # print(data2)
            for instance in data1:
                # 应该是影响力
                ys.append(instance.Influence)
            for instance in data2:
                # 应该是影响力
                xs.append(instance.Influence)
            return xs, ys