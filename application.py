from flask import Flask, render_template, jsonify
import base64
import io
from PIL import Image
import keras
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
import numpy as np

#export  FLASK_APP=app.py
#python3 -m flask run


app = Flask(__name__,static_url_path='/static')


global model
model = tf.keras.models.load_model("/Users/odiaz/covid_proj/COVID-19-Predictor/cnn_covid_x-ray_v1.h5")
print("* Model loaded!")


@app.route('/',)
def main():
   print('***in main')
   data = {'diagnosis': 0}
   return render_template('Covid-19_SelfTest.html', data = data) # this renders the html template


@app.route ('/ans' , methods = ['POST'])
def pred():
   if request.method == 'POST':
      message = request.get_json(force=True)
      print('message')
      encoded = message['image']  # assign value associated with key called image in message
      decoded = base64.b64decode(encoded)
      image = Image.open(io.BytesIO(decoded)) 

      image = image.convert("RGB")   # resize func outside of func from vid
      image = image.resize((64, 64)) 
      image = img_to_array(image)
      image = np.expand_dims(image, axis=0)
 
      # need to 


      #image = tf.image.decode_png(tf_image, channels=3)#in predict func   got to here last time then couldn't cnvert to 
      #image = tf.image.resize(image, [64, 64])
      #image = tf.expand_dims(image, axis=0)
      result = model.predict_classes(image)[0][0] # RETURN line in function
       
      #ValueError: Attempt to convert a value (<PIL.PngImagePlugin.PngImageFile image mode=L 
      # size=1024x1024 at 0x14F4F3400>) with an unsupported type (<class 'PIL.PngImagePlugin.PngImageFile'>) to a Tensor.

      response = { 'prediction':{
      'covid': int(result)
         }
      }


      return jsonify(response)

if __name__ == '__main__':
   app.run(host='0.0.0.0',port="8400",debug=True)








