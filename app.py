from flask import Flask, render_template, url_for, jsonify
import os
import base64
import numpy as np
import io
from PIL import Image
import keras
from keras import backend as K
from keras. models import Sequential
from keras. models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask
from tensorflow import keras
import tensorflow as tf
import sys


app = Flask(__name__,static_url_path='/static')

def get_model():
   global model
   model = tf.keras.models.load_model("cnn_covid_x-ray_v1.h5")
   print("* Model loaded!")


@app.route('/')
def home():
    return render_template('Covid-19 SelfTest.html') # this renders the html template
'''
@app.route("/predict", methods=["POST"])   #from https://youtu.be/XgzxH6G-ufA, uses jquery in html file for var
def predict():
   message = request.get_json(force=True)
   encoded = message['image']
   decoded = base64.664decode(encoded)
   image = Image.open(io.ByteslO(decoded))
   processed_image = preprocess_image(image, target_size=(224, 224))

   prediction = model.predict(processed_image).tolist()

   response = {
      'prediction':{
         'dog': prediction[0][0],
         'cat': prediction[0][1]
         }
    }

   return jsonify(response)



@app.route("/result", methods=["GET", "POST"])
def my_function():
    if request.method == "POST":
        data = {}    # empty dict to store data
        data['uploadImg'] = request.json['title']
        data['release_date'] = request.json['movie_release_date']

       # do whatever you want with the data here e.g look up in database or something
       # if you want to print to console

        print(data, file=sys.stderr)

        # then return something back to frontend on success

        #this returns back received data and you should see it in browser console
        # because of the console.log() in the script.
        return jsonify(data)
'''


@app.route ('/ans' , methods = ['GET','POST'])
def pred():
    if request.method == 'POST':
        get_model()

        file = request.files['xray'] #requests files input in html
        file.filename = "upload.jpeg" #makes file class attribute file name upload.jpeg
        file_name = file.filename     #makes var file_name = "upload.jpeg"
        base = os.path.dirname(__file__)  # gets directory to current file
        filepath = os.path.join(base, 'uploads', file.filename) # idk
        print(filepath)

        image = tf.io.read_file('filepath')
        image = tf.image.decode_png(image, channels=3)
        image = tf.image.resize(image, [64, 64])
        image = tf.expand_dims(image, axis=0)   # the shape would be (1, 64, 64, 3)
        result = model.predict_classes(image)[0][0]

        file.save(filepath)

        result = predict()
        if result == 0:
          print("COVID-19")
        else:
          print("NORMAL")

'''
    data_gen= ImageDataGenerator(rescale=1/255).flow_from_directory(base,classes=["uploads"],class_mode=None, target_size=(100,100))
    predi = (model.predict(data_gen))
    message = str(round(predi[0][1]*100,2))+"%"
    return render_template("products.html",likelyhood = message)
'''
if __name__ == 'name':
    app.run(debug=true)
