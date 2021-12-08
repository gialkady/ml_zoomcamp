#!/usr/bin/env python
# coding: utf-8


import tflite_runtime.interpreter as tflite
import numpy as np
import os

from io import BytesIO
from urllib import request

from PIL import Image

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def prepare_input(x):
    return x / 255.0

MODEL_NAME = os.getenv('MODEL_NAME', 'dogs_cats.tflite')

interpreter = tflite.Interpreter(model_path=MODEL_NAME)
#load the weights from model to the memory (keras done this automatically)
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

#url='https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg'



def predict(url):
    img=download_image(url)
    img=prepare_image(img, target_size =(150,150))

    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)


    interpreter.set_tensor(input_index, X) # put input in the interpreter
    interpreter.invoke() #model work


    preds = interpreter.get_tensor(output_index) #get or fetch output

    return float(preds[0, 0])



def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {
        'prediction': pred
    }

    return result

