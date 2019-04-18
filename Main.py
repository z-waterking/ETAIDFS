# coding:utf-8
from flask import Flask,render_template,url_for,redirect
import flask
import json
from flask import request
import config
app = Flask(__name__)
app.config.from_object(config)

@app.route('/newpage_index',methods=['POST','GET'])
def GetNewPage_index():
    return render_template('index.html')

@app.route('/ExpertInformationManage',methods=['POST','GET'])
def GetPage_ExpertInformationManage():
    return render_template('ExpertInformationManage.html')

@app.route('/login',methods=['POST','GET'])
def GetPage_login():
    return render_template('login.html')

@app.route('/new_page',methods=['POST','GET'])
def GetNewPage():
    A = request.args.get("a")
    B = request.args.get("b")
    print("--------------GETNEWPAGE-------------")
    print(A)
    print(B)
    return render_template('NewPage.html', data = {"result":"OK"})

@app.route('/post_data',methods=['POST','GET'])
def PostData():
    data = request.json
    print("-------------POST-----------")
    print(data)
    return json.dumps({"result":"完成测试"})

@app.route('/get_data',methods=['POST','GET'])
def Data():
    A = request.args.get("a")
    B = request.args.get("b")
    print("--------------GET-------------")
    print(A)
    print(B)
    return json.dumps({"result":"完成测试"})

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)

