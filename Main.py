from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory
from functools import wraps
from module import *
import os,time,decimal
from werkzeug.utils import secure_filename
from flask_admin import Admin
app = Flask(__name__)

app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:catherine@127.0.0.1:1433/EmergingTechnologyForecastDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'catherine'
app.config["SQLALCHEMY_ECHO"] = True
#上传文件存放位置
UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['txt','pdf','doc','docx','png','jpg','gif','xls','xlsx','pptx','ppt','zip'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
admin = Admin(app)

#辅助函数
#登录检验
def valid_login(email, password):
    dbsession = DatabaseManagement()
    query_filter = and_(User.email == email, User.password == password)
    user = dbsession.query_all(User, query_filter)
    if user:
        return True
    else:
        return False
#注册检验
def valid_register(username, email):
    dbsession = DatabaseManagement()
    query_filter = or_(User.username == username, User.email == email)
    user = dbsession.query_all(User, query_filter)
    if user:
        return False
    else:
        return True

#登录
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('email'):
            return func(*args, **kwargs)
        else:
            return redirect('login.html')
    return wrapper
#上传文件需要函数
def allowed_file(filename):
    return '.'in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/index',methods=['POST','GET'])
def GetPage():
    return render_template('homepage.html')

@app.route('/index2',methods=['POST','GET'])
def GetPage2():
    return render_template('index.html')

@app.route('/new_page', methods=['POST', 'GET'])
def GetNewPage():
    A = request.args.get("a")
    B = request.args.get("b")
    print("--------------GETNEWPAGE-------------")
    print(A)
    print(B)
    return render_template('NewPage.html', data={"result":"OK"})

@app.route('/newpage_index', methods=['POST','GET'])
@login_required
def GetNewPage_index():
    return render_template('index.html')

@app.route('/ExpertInformationManage',methods=['POST','GET'])
@login_required
def GetPage_ExpertInformationManage():
    return render_template('ExpertInformationManage.html')

@app.route('/register', methods=['POST','GET'])
def GetPage_register():
    if request.method == 'POST':
        if request.form["password1"] != request.form["password2"]:
            flash('两次密码不一致，请重新输入！')
        elif valid_register(request.form["username"], request.form["email"]):
            user = User(username=request.form["username"], password=request.form["password1"], email=request.form["email"])
            dbsession1 = DatabaseManagement()
            dbsession1.add_obj(user)
            flash("成功注册！")
            return redirect(url_for("GetPage_login"))
        else:
            flash("该用户名或邮箱已被注册！")

    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def GetPage_login():
    if request.method == 'POST':
        if valid_login(request.form["email"], request.form["password"]):
            email = request.form["email"]
            flash('登录成功!')
            session['email'] = request.form["email"]
            return redirect(url_for("GetPage"))
        else:
            flash('用户名或密码错误！')

    return render_template('login.html')
#-----------系统简介---------------
@app.route('/GetIntroduction', methods=['POST','GET'])
def SysIntroduction():
    FirstDirectory = request.args.get("FirstDirectory")
    result = sysIntroduction(FirstDirectory)
    return json.dumps({'introduction':result})

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
    saveJudgeResult(data)
    result = {}
    result['success'] = True
    return json.dumps(result)
#-----------专家提交数据End---------------

#-----------获取通用数据------------------
#获取通用的国家
@app.route('/GetCommonCountrys',methods=['POST','GET'])
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

#-----------获取通用数据End---------------

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)

#-----------获取图表展示数据--------------
@app.route('/GetTotalData',methods=['POST','GET'])
def GetTotalData():
    data = request.json
    print(data)
    #todo 根据前端请求查询对应的数据库
    #组织最后的数据
    ThirdClass = data["ThirdClass"]
    ThirdDirectory = data["ThirdDirectory"]
    ForthDirectory = data["ForthDirectory"]
    xs, ys = gettotalData(ThirdClass, ThirdDirectory, ForthDirectory)
    print(xs, ys)
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
        result['label'] = ['Develop', 'Initial', 'Growup', 'Expand', 'Mature']
    else:
        # result['xs'] = [2008, 2009, 2010, 2011, 2012, 2013]
        # result['ys'] = [23, 34, 56, 29, 56, 78]
        result['graph'] = 'line'
        result['stage'] = ['Develop', 'Initial', 'Growup', 'Expand', 'Mature', 'Mature']
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
    xs, ys = gettotalCountryData(ThirdClass, ThirdDirectory, ForthDirectory, Country)
    print(xs, ys)
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
        result['label'] = ['Develop', 'Initial', 'Growup', 'Expand', 'Mature']
    else:
        # result['xs'] = [2008, 2009, 2010, 2011, 2012]
        # result['ys'] = [110, 123, 130, 140, 150]
        result['graph'] = 'line'
        result['stage'] = ['Develop', 'Initial', 'Growup', 'Expand', 'Mature']
    return json.dumps(result, cls=DecimalEncoder)
#-----------获取图表展示数据End---------------

#-----------监测报告上传----------------
@app.route('/upload', methods=['POST','GET'])
def upload_file():
    return render_template('upload.html')
@app.route('/GetLoad',methods=['POST','GET'])
def GetLoad():
    file_dir = os.path.join(basedir,app.config['UPLOAD_FOLDER'])
    #文件夹不存在就创建
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    #从表单的myfile获取文件
    f = request.files["myfile"]
    #未选择文件
    # if f == '':
    #     return redirect(url_for("upload_file"))
    #不能同时上传两个文件

    #判断是否为上传文件允许类型
    if f and allowed_file(f.filename):
        fname = f.filename
        #获取文件后缀
        ext = fname.rsplit('.',1)[1]
        unix_time = int(time.time())
        #修改文件名
        new_filename = str(unix_time)+'.'+ ext
        #上传文件名即为(中文名)时间
        f.save(os.path.join(file_dir,new_filename))
        result = {}
        result['errno'] = 0
        result['errmsg'] = "上传成功"
        return json.dumps(result)
    else:
        result = {}
        result['errno'] = 1001
        result['errmsg'] = "上传失败"
        return json.dumps(result)

@app.route('/getdata',methods=['POST','GET'])
def GetData():
    data = request.json
    print('----')
    print(data)
    return json.dumps(data)

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)