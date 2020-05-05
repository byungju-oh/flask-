#import torch
import sys
import cv2
import tensorflow.keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image, ImageOps
import numpy as np
from flask import Flask, redirect, url_for, request, render_template
#파일 업로드

import glob
#파일이름 보호
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
import os


app = Flask(__name__)
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
print('model')
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
def pred(img_path,model):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
    #image = Image.open('C:/Users/qkd/python/capst/uploads/표준남자8.jpg')
    image = Image.load_img('img_path')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
    image_array = np.asarray(image)

# display the resized image
    #image.show()

# Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
    data[0] = normalized_image_array

# run the inference
    prediction = model.predict(data)
    return prediction

@app.route("/",methods=['GET'])
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
#메인 모듈로 실행될 때 플라스크 서버 구동
if __name__ == "__main__":
    app.run(debug=True)
