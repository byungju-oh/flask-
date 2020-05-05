from flask import Flask, redirect, url_for, request, render_template
#파일 업로드

import glob
#파일이름 보호
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
import os

app = Flask(__name__)

@app.route("/")

def index():

    return render_template('index.html')
@app.route("/predict",methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['file']

        basepath = os.path.dirname['file']
        file_path = os.path.join(basepath,'uploads',secure_filename(f.filename))
        f.save(file_path)

        preds = pred(file_path,model)
        pred_class = decode_predictions(preds, top=1)
        result = str(pred_class[0][0][1])             
        return result

    return None




if __name__ == "__main__":
    app.run()
