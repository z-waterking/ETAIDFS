from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory
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


#上传文件需要函数
def allowed_file(filename):
    return '.'in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

#打开新链接的模版
@app.route('/new_page', methods=['POST', 'GET'])
def GetNewPage():
    A = request.args.get("a")
    B = request.args.get("b")
    print("--------------GETNEWPAGE-------------")
    print(A)
    print(B)
    return render_template('NewPage.html', data={"result":"OK"})


#页面测试
@app.route('/normal', methods=['POST', 'GET'])
def GetNormal():
    return render_template('homepage_normalUser.html')

@app.route('/expert', methods=['POST', 'GET'])
def GetExpert():
    return render_template('homepage_Expert.html')

@app.route('/admin', methods=['POST', 'GET'])
def GetAdmin():
    return render_template('homepage_Administrator.html')
#页面测试END

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    from LoginAndRegister import *
    from ExpertJudgeAndInformationManager import *
    from GetCommonData import *
    from ShowGraphData import *
    from UploadFile import *
    app.run(debug=True)
