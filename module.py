from DBsession import *
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

#获取通用的年份




#直接获取大类
def CommonSecondaryClass():
    CommonSecondaryClass = []
    dbsession = DatabaseManagement()
    query_filter = DictClas.Code.like('00_')
    secondaryclass = dbsession.query_all(DictClas, query_filter)
    for data in secondaryclass:
        CommonSecondaryClass.append(data.Class)
    #根据data.Subsys返回石墨orAIor3D打印
    return CommonSecondaryClass

#通过大类获取小类
def FindThirdClassBySecondaryClass(SecondaryClass):
    FindThirdClassBySecondaryClass = []
    dbsession = DatabaseManagement()
    # secondaryclass = dbsession.execute_sql("select * from Dict_Class where Code like '001___'")
    query_filter1 = DictClas.Code.like('00____')
    secondaryclass = dbsession.query_all(DictClas, query_filter1)
    for data in secondaryclass:
        FindThirdClassBySecondaryClass.append(data.Class)
    return FindThirdClassBySecondaryClass

#-----------获取图表展示数据--------------

