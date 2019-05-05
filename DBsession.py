from sqlalchemy import create_engine, and_, update, or_
from sqlalchemy.orm import sessionmaker
from model import *
class DatabaseManagement():

    def __init__(self):
        self.engine = create_engine("mssql+pyodbc://sa:catherine@127.0.0.1:1433/EmergingTechnologyForecastDB?driver=SQL+Server+Native+Client+11.0",echo=True)
        DBsession = sessionmaker(bind=self.engine)
        self.session = DBsession()

    def add_obj(self, obj):
        self.session.add(obj)
        self.session.commit()
        return obj

    def query_all(self, target_class, query_filter):
        result_list = self.session.query(target_class).filter(query_filter).all()
        return result_list

    def update_by_fliter(self, obj_class, update_hash, query_filter):
        self.session.query(obj_class).filter(query_filter).update(update_hash)
        self.session.commit()

    def delete_by_filter(self, obj_class, query_filter):
        self.session.query(obj_class).filter(query_filter).delete()
        self.session.commit()

    def close(self):
        self.session.close()

    def execute_sql(self, sql_str):
        return self.session.execute(sql_str)


if __name__ == "__main__":
    myData = DatabaseManagement()
    expert1 = ExpertList(Expert_Name = "王",Birth_Year="1975",Sex="男",People="汉族",Institution="院士",Professional_Title="muji",
                         Administrative_duty = "jjj",City="上海",Province="上海",Address="浦东新区",Zip="",
                         Highestdegree = "博士",Degreedate = "2006",University="北理",Honorary_Reward="",
                         Tel="123456789",Email="1051778789@163.com",Class ="")
    expert2 = ExpertList(Expert_Name="刘", Birth_Year="1972", Sex="女", People="汉族", Institution="教授",
                         Professional_Title="muji",
                         Administrative_duty="muji", City="北京", Province="北京", Address="中关村", Zip="",
                         Highestdegree="博士", Degreedate="2006", University="中科院", Honorary_Reward="",
                         Tel="123456789", Email="1051778789@163.com", Class="")
    #增加
    user = User(username='王若琳', email='1051776737@qq.com',password='123456')
    myData.add_obj(user)
    # myData.add_obj(expert2)
    #查询
    # query_filter = and_(ExpertList.ID == 5)
    # query_list = myData.query_all(Country, query_filter)
    # for i in query_list:
    #     print(i.ID, i.Country)
    #更改
    # query_filter = or_(ExpertJudge.Id == 1, ExpertList.Id == 2)
    # update_hash = {ExpertList.Country: "China"}
    # myData.update_by_fliter(ExpertList, update_hash, query_filter)
    # #删除
    # query_filter = or_(ExpertList.Expert_Name == "刘", ExpertList.Expert_Name == "王")
    # myData.delete_by_filter(ExpertList, query_filter)
    #执行SQL语句
    # dbs = myData.execute_sql("SELECT NAME FROM USER ")

