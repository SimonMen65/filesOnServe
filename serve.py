from flask import Flask, render_template, request, redirect, send_file
from flask.helpers import url_for
from back import FilesAnubis
from flaskext.mysql import MySQL
import os
import io

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'FilesAnubis'
db = MySQL(app)

fa = FilesAnubis()
fa.setNewID()

@app.route('/')
def index():
    files_info = fa.viewFiles()
    return render_template('index.html',info = files_info)

@app.route('/process',methods = ['POST'])
def upload():
    file = request.files.get('file')
    fa.uploadFile(file.read(),file.filename)
    return redirect('/') 

@app.route('/download/<id_num>',methods = ['GET'])
def download(id_num):
    file = fa.getFile(id_num[1:])
    return send_file(io.BytesIO(file['file']),as_attachment=True,download_name = file['name'])
    
@app.route('/remove/<id_num>')
def remove(id_num):
    fa.removeFile(id_num[1:])
    return redirect("/")

if __name__ == '__main__':
    app.run()