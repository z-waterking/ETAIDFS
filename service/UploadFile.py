from service.Main import *
from flask import Flask, json, config,render_template, url_for, redirect, flash
from flask import request,jsonify,session,send_from_directory
from service.model import *
from service.DBsession import *
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
        ext = fname.rsplit('.', 1)[1]
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
