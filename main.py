from flask import *
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def create_app():
   return "hello"
   #return redirect('output/sample_data_premium.csv')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      os.system("python3 malware_v7.py "+f.filename)
      path = "output/"+f.filename
      return send_file(path, as_attachment=True)
      #return redirect('output/' + f.filename)
