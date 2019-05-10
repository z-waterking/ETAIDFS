from DBsession import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, and_, update, or_
from model import *
#-------------专家提交数据-------------






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
    print('------', CommonSecondaryClass)
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

