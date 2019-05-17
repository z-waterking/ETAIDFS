from Main import *
from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory
from model import *
from DBsession import *
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)

#-----------获取图表展示数据--------------
@app.route('/GetTotalData', methods=['POST','GET'])
def GetTotalData():
    data = request.json
    print(data)
    #todo 根据前端请求查询对应的数据库
    #组织最后的数据
    ThirdClass = data["ThirdClass"]
    ThirdDirectory = data["ThirdDirectory"]
    ForthDirectory = data["ForthDirectory"]
    xs, ys, label = gettotalData(ThirdClass, ThirdDirectory, ForthDirectory)
    print(xs, ys, label)
    result = {}
    result['xs'] = xs
    result['ys'] = ys
    result['success'] = True
    result['graph'] = 'line'
    result['title'] = '{} {}领域-{}总体趋势'.format(data['SecondaryClass'], data['ThirdClass'], data['ThirdDirectory'])
    print(result)
    # 如果是这个目录下的，则为散点图。否则为折线图。
    # 散点图不需要管stage的值。折线图需要管。
    if data['SecondDirectory'].strip() == '科学与技术发展关联聚类监测':
        # result['xs'] = [200, 309, 421, 20, 402]
        # result['ys'] = [110, 123, 130, 140, 150]
        result['graph'] = 'plot'
        result['label'] = label
    else:
        # result['xs'] = [2008, 2009, 2010, 2011, 2012, 2013]
        # result['ys'] = [23, 34, 56, 29, 56, 78]
        result['graph'] = 'line'
        #取出的label命名为stage
        result['stage'] = label
    return json.dumps(result, cls=DecimalEncoder)

#-----------获取图表展示数据End---------------


@app.route('/GetCountryData', methods=['POST','GET'])
def GetCountryData():
    data = request.json
    #{'FirstDirectory': '3D打印技术监测', 'SecondDirectory': '科学发展与产业化阶段关联趋势', 'ThirdDirectory': '科学热度与产业化阶段关联趋势', 'ForthDirectory': '国家分析', 'SecondaryClass': 'B', 'ThirdClass': '小类2', 'Country': 'US'}
    print(data)
    #todo 根据前端请求查询对应的数据库
    #组织对应的数据
    ThirdClass = data["ThirdClass"]
    ThirdDirectory = data["ThirdDirectory"]
    ForthDirectory = data["ForthDirectory"]
    Country = data["Country"]
    xs, ys, label = gettotalCountryData(ThirdClass, ThirdDirectory, Country)
    print(xs, 'aaa', ys)
    result = {}
    result['xs'] = xs
    result['ys'] = ys
    result['success'] = True
    result['graph'] = 'line'
    result['title'] = '{} {}领域-{}趋势-{}'.format(data['SecondaryClass'], data['ThirdClass'], data['ThirdDirectory'], data['Country'])
    # 如果是这个目录下的，则为散点图。否则为折线图。
    # 散点图不需要管stage的值。折线图需要管。
    if data['SecondDirectory'].strip() == '科学与技术发展关联聚类监测':
        # result['xs'] = [200, 309, 421, 20, 402]
        # result['ys'] = [110, 123, 130, 140, 150]
        result['graph'] = 'plot'
        result['label'] = label
    else:
        # result['xs'] = [2008, 2009, 2010, 2011, 2012]
        # result['ys'] = [110, 123, 130, 140, 150]
        result['graph'] = 'line'
        result['stage'] = label
    return json.dumps(result, cls=DecimalEncoder)
#-----------获取图表展示数据End---------------