from flask import Flask, render_template, request, redirect, send_file
from back import FilesAnubis
import os
import io

app = Flask(__name__)
fa = FilesAnubis()
fa.setNewID()

@app.route('/')
def index():
    files_info = fa.viewFiles()
    print(files_info)
    return render_template('index.html',info = files_info)

@app.route('/process',methods = ['POST'])
def upload():
    pichead = request.files.get('file')
    print(pichead)
    fa.uploadFile(pichead,pichead.filename)
    return redirect('/')

@app.route('/download/<id_num>',methods = ['GET'])
def download(id_num):
    file = fa.getFile(id_num[1:])
    #return send_file(io.BytesIO(file['file']),as_attachment=True,download_name=file['name'])
    #file['file'].save(os.path.join("./images/"))
    return send_file(io.BytesIO(file['file']),as_attachment=True,mimetype='image/jpeg',download_name = file['name'])
    

if __name__ == '__main__':
    app.run()