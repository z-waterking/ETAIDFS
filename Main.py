from flask import Flask,render_template,url_for,redirect
import flask
import json
from flask import request
import config
app = Flask(__name__)
app.config.from_object(config)

@app.route('/index',methods=['POST','GET'])
def GetPage():
    return render_template('index.html')

@app.route('/getdata',methods=['POST','GET'])
def GetData():
    data = request.json
    print('----')
    print(data)
    return json.dumps(data)

if __name__ == '__main__':
    # app.run(host='192.168.1.103',port='8080',debug=True)
    app.run(debug=True)

