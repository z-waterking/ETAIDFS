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

@app.route('/getdata',methods=['POST','GET'])
def GetData():
    data = request.json
    print('----')
    print(data)
    return json.dumps(data)

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)
