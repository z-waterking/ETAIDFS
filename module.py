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


# -------------专家提交数据-------------
def saveJudgeResult(data):
    thirdClass = data['ThirdClass']
    ExpertName = '王'
    # 获取专家每个阶段判断年份，在数据库中标识年份对应阶段
    # 获取developstage年份
    stages = ['DevelopStage', 'InitialStage', 'GrowupStage', 'ExpandStage', 'MatureStart']
    for i in range(len(stages)):
        developStart = int(data[stages[i]]['start'])
        developEnd = int(data[stages[i]]['stop'])
        YearList = list(range(developStart, developEnd+1))
        for year in YearList:
            # 年 就是year
            # 小类
            # 阶段,数据库中存的是1,2,3,4,5
            stage = i + 1
            # 先查 小类+年份+专家
            dbsession = DatabaseManagement()
            query_filter = and_(ExpertJudge.Class == thirdClass, ExpertJudge.Expert == ExpertName,
                                ExpertJudge.Year == year)
            expert_judge = dbsession.query_all(ExpertJudge, query_filter)
            # 如果结果为空，直接添加：
            # 添加专家姓名和阶段
            print('********', expert_judge)
            if expert_judge == []:
                add_expert = ExpertJudge(Class=thirdClass, Expert=ExpertName, Year=year, Stage=stage)
                dbsession.add_obj(add_expert)
            else:
                # 如果查询结果不为空，直接更新阶段
                update_hash = {ExpertJudge.Stage: stage}
                dbsession.update_by_fliter(ExpertJudge, update_hash, query_filter)


# -------------获取通用数据-------------
# 获取通用的国家
def CommonCountrys():
    CommonCountrys = []
    dbsession = DatabaseManagement()
    query_filter = Country.ID >= 1
    country = dbsession.query_all(Country, query_filter)
    for data in country:
        CommonCountrys.append(data.Country)
    return CommonCountrys


# 直接获取大类
def CommonSecondaryClass(Firstdirectory):
    CommonSecondaryClass = []
    dbsession = DatabaseManagement()
    if Firstdirectory == '3D打印技术监测':
        query_filter = and_(DictClas.Code.like('00_'), DictClas.Subsys == '002')
    elif Firstdirectory == '碳纳米管与石墨烯监测':
        query_filter = and_(DictClas.Code.like('00_'), DictClas.Subsys == '003')
    else:
        query_filter = and_(DictClas.Code.like('00_'), DictClas.Subsys == '001')
    secondaryclass = dbsession.query_all(DictClas, query_filter)
    for data in secondaryclass:
        CommonSecondaryClass.append(data.Class)
    return CommonSecondaryClass


# 通过大类获取小类
def FindThirdClassBySecondaryClass(SecondaryClass):
    FindThirdClassBySecondaryClass = []
    dbsession = DatabaseManagement()
    query_filter = and_(DictClas.Class == SecondaryClass, DictClas.Code.like('00_'))
    secondaryclass = dbsession.query_all(DictClas, query_filter)
    for instance in secondaryclass:
        secondaryclasscode = instance.Code
        secondarySubclass = instance.Subsys
        print(secondaryclasscode)
    query_filter1 = and_(DictClas.Code.like('%s%%%%' % secondaryclasscode), DictClas.Code.like('00____'),
                         DictClas.Subsys == secondarySubclass)
    findthirdclass = dbsession.query_all(DictClas, query_filter1)
    # findthirdclass = dbsession.execute_sql("select * from Dict_Class where Code like '%s%%%%'" % secondaryclasscode)
    for data in findthirdclass:
        FindThirdClassBySecondaryClass.append(data.Class)

    return FindThirdClassBySecondaryClass


# -----------获取图表展示数据--------------
def gettotalData(ThirdClass, ThirdDirectory, ForthDirectory):
    #根据三级目录找到表名
    WayFindTable = {
        '科学发展热度与产业发展阶段关联趋势': [PaperHotDegree, 'hot'],
        '科学发展影响力与产业发展关联趋势' : [PaperInfluence, 'influence'],
        '技术发展热度与产业发展阶段关联趋势' : [PatentHotDegree, 'hot'],
        '技术发展影响力与产业发展阶段关联趋势' : [PatentInfluence, 'influence']
    }
    WayFindClusterTable = {
        '科学热度与技术热度关联聚类监测': [PatentHotDegree, PaperHotDegree, 'hot'],
        '科学影响力与技术影响力聚类关联分析' : [PatentInfluence, PaperInfluence, 'influence']
    }
    StageName = ['', 'Develop', 'Initial', 'Growup', 'Expand', 'Mature']
    if '聚类' not in ThirdDirectory:
        #取得对应的表名
        Table = WayFindTable[ThirdDirectory][0]
        # 去表PaperHotDegree查
        dbsession = DatabaseManagement()
        query_filter = and_(Table._class == ThirdClass)
        datas = dbsession.query_order_by(Table, query_filter, "year")
        # print(data)
        # 在ExpertJudge查对应年份所对应stage
        query_filter1 = and_(ExpertJudge.Class == ThirdClass)
        all_datas = dbsession.query_order_by(ExpertJudge, query_filter1, "year")
        return FormNonClusterData(datas, all_datas, WayFindTable, ThirdDirectory, StageName)
    else:
        #取得要查的两个表
        Table1 = WayFindClusterTable[ThirdDirectory][0]
        Table2 = WayFindClusterTable[ThirdDirectory][1]
        # 去表PaperHotDegree和表PatentHotDegree查
        dbsession = DatabaseManagement()
        query_filter1 = and_(Table1._class == ThirdClass)
        query_filter2 = and_(Table2._class == ThirdClass)
        data1 = dbsession.query_order_by(Table1, query_filter1, "year")
        data2 = dbsession.query_order_by(Table2, query_filter2, "year")
        return FormClusterData(data1, data2, WayFindClusterTable, ThirdDirectory)

def gettotalCountryData(ThirdClass, ThirdDirectory, Country):
    # 根据三级目录找到表名
    WayFindTable = {
        '科学发展热度与产业发展阶段关联趋势': [PaperCountryHotDegree, 'hot'],
        '科学发展影响力与产业发展关联趋势': [PaperCountryInfluence, 'influence'],
        '技术发展热度与产业发展阶段关联趋势': [PatentCountryHotDegree, 'hot'],
        '技术发展影响力与产业发展阶段关联趋势': [PatentCountryInfluence, 'influence']
    }
    WayFindClusterTable = {
        '科学热度与技术热度关联聚类监测': [PatentCountryHotDegree, PaperCountryHotDegree, 'hot'],
        '科学影响力与技术影响力聚类关联分析': [PatentCountryInfluence, PaperCountryInfluence, 'influence']
    }
    StageName = ['', 'Develop', 'Initial', 'Growup', 'Expand', 'Mature']
    if '聚类' not in ThirdDirectory:
        # 取得对应的表名
        Table = WayFindTable[ThirdDirectory][0]
        # 去表PaperHotDegree查
        dbsession = DatabaseManagement()
        query_filter = and_(Table._class == ThirdClass, Table.country == Country)
        datas = dbsession.query_order_by(Table, query_filter, "year")
        # print(data)
        # 在ExpertJudge查对应年份所对应stage
        query_filter1 = and_(ExpertJudge.Class == ThirdClass)
        all_datas = dbsession.query_order_by(ExpertJudge, query_filter1, "year")
        return FormNonClusterData(datas, all_datas, WayFindTable, ThirdDirectory, StageName)
    else:
        # 取得要查的两个表
        Table1 = WayFindClusterTable[ThirdDirectory][0]
        Table2 = WayFindClusterTable[ThirdDirectory][1]
        # 去表PaperHotDegree和表PatentHotDegree查
        dbsession = DatabaseManagement()
        query_filter1 = and_(Table1._class == ThirdClass, Table1.country == Country)
        query_filter2 = and_(Table2._class == ThirdClass, Table2.country == Country)
        data1 = dbsession.query_order_by(Table1, query_filter1, "year")
        data2 = dbsession.query_order_by(Table2, query_filter2, "year")
        return FormClusterData(data1, data2, WayFindClusterTable, ThirdDirectory)

#格式化非聚类的目录中查找的元素，返回前端显示
def FormNonClusterData(datas, all_datas, WayFindTable, ThirdDirectory, StageName):
    '''

    :param datas: 数据集合，提供x，y
    :param all_datas: 专家判断集合，提供上一个参数的阶段判断结果
    :param WayFindTable: 一个dict,寻找查找哪个表的
    :param ThirdDirectory: 三级目录判断是热度还是影响力
    :param StageName: 将数据库中的1-5年份阶段判断转化为英文表示
    :return: 格式化好的非聚类数据
    '''
    # todo zsf 根据取得的数据确定一份最终数据
    # 根据 i 的值返回 Stage的值
    # 收集每一年份的所有人判断的专家数据，如下：
    xs = []
    ys = []
    label = []
    # 专家判断表中的年份收集
    YearStageCollect = {}
    # 最终阶段年份收集
    YearStage = {}
    # 最终的年份—y
    YearValues = {}
    # 所有存在的年份收集,及其
    AllYears = []
    for data in datas:
        if WayFindTable[ThirdDirectory][1] == 'hot':
            YearValues[int(data.year)] = data.Hot_degree
        else:
            YearValues[int(data.year)] = data.Influence
    AllYears = list(YearValues.keys())
    AllYears.sort()
    # 去挑选对应年份的阶段判断数据
    for year in AllYears:
        YearStageCollect[year] = []
    for data in all_datas:
        # 由于数据表数据缺失，判断完成之后，可能有些领域没有数据，但却有了专家判断的结果
        # 在此予以规避
        if int(data.Year) in AllYears:
            YearStageCollect[int(data.Year)].append(data.Stage)

    # 找出每个stage里面最多的,加入stage
    def FindMaxFrequency(li):
        '''
        :param li: 待寻找列表
        :return: 返回1-5，表明阶段，否则，表明列表为空
        '''
        if len(li) == 0:
            return -1
        Stage2Count = {}
        for l in li:
            if l not in Stage2Count:
                Stage2Count[l] = 0
            Stage2Count[l] += 1
        Stages = list(Stage2Count.keys())
        Stages.sort(key=lambda x: Stage2Count[x])
        return Stages[-1]

    for year in AllYears:
        st = FindMaxFrequency(YearStageCollect[year])
        # 如果第一个年份中就没有人判断数据
        index = AllYears.index(year)
        if st == -1:
            if index == 0:
                st = 1
            else:
                # 赋值为上一个判断过的阶段
                st = YearStage[AllYears[index - 1]]
        YearStage[year] = st
    # 整理得到的数据
    xs = AllYears
    for year in AllYears:
        ys.append(YearValues[year])
        label.append(StageName[YearStage[year]])
    return xs, ys, label

#格式化聚类目录中的元素
def FormClusterData(data1, data2, WayFindClusterTable, ThirdDirectory):
    '''

    :param data1: 科学热度或者科学影响力，作为y轴
    :param data2: 技术热度或者技术影响力，作为x轴
    :param WayFindClusterTable: 一个dict，寻找待查找的表
    :param ThirdDirectory: 对应的三级目录，是热度还是影响力
    :return: 格式化完成的xs, ys, label
    '''
    xs = []
    ys = []
    label = []
    # 收集两个年份-值数据
    YearX = {}
    YearY = {}
    # 加入数据
    for instance in data1:
        # 应该是科学热度，科学影响力
        if WayFindClusterTable[ThirdDirectory][2] == 'hot':
            YearY[int(instance.year)] = instance.Hot_degree
        else:
            YearY[int(instance.year)] = instance.Influence
    for instance in data2:
        # 技术热度或者是技术影响力
        if WayFindClusterTable[ThirdDirectory][2] == 'hot':
            YearX[int(instance.year)] = instance.Hot_degree
        else:
            YearX[int(instance.year)] = instance.Influence
    # 整合YearX和YearY的数据
    # 所有年份
    AllYears = []
    AllYears.extend(list(YearX.keys()))
    AllYears.extend(list(YearY.keys()))
    AllYears = list(set(AllYears))
    # 整合最后的数据
    for year in AllYears:
        label.append(year)
        x = 0
        y = 0
        if year in YearX:
            x = YearX[year]
        if year in YearY:
            y = YearY[year]
        xs.append(x)
        ys.append(y)
    return xs, ys, label