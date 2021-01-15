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


app = Flask(__name__,static_url_path='/static')


global model
model = tf.keras.models.load_model("cnn_covid_x-ray_v1.h5")
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

      '''def predict():    # from PM
         image = tf.io.read_file('/content/NORMAL(1337).png')
         image = tf.image.decode_png(image, channels=3)
         image = tf.image.resize(image, [64, 64])
         image = tf.expand_dims(image, axis=0)   # the shape would be (1, 64, 64, 3)
         return model.predict_classes(image)[0][0] '''

      




      
   

      #return render_template('Covid-19_SelfTest.html', data=data)

   '''
  data = {'diagnosis': 0}
  if request.method == 'POST':
    print('yyyyy')
    get_model()

    file = request.files['image'] #requests file the file that was inputed in html   # from Danial
    file.filename = "upload.jpeg" #makes file class attribute file name upload.jpeg
    file_name = file.filename     #makes var file_name = "upload.jpeg"
    base = os.path.dirname(__file__)  # gets directory to current file
    filepath = os.path.join(base, 'uploads', file.filename) # idk
    print(filepath)

    image = tf.io.read_file('filepath')         # from PM Nelaven
    image = tf.image.decode_png(image, channels=3)
    image = tf.image.resize(image, [64, 64])
    image = tf.expand_dims(image, axis=0)   # the shape would be (1, 64, 64, 3)
    result = model.predict_classes(image)[0][0]

    file.save(filepath)

    result = predict()
    if result == 0:       
      data['diagnosis'] = 0
    else:
      data['diagnosis'] = 1
   '''



if __name__ == '__main__':
   app.run(debug = True)








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
