import os
import sys
import csv

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename

# Some utilites
import numpy as np
#from util import base64_to_pil
from PIL import Image

from io import BytesIO
import base64

app = Flask(__name__, template_folder='templates')

#model = pickle.load(open('../model/model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/who', methods=['GET'])
def who():
    return render_template('who.html')






## image upload 

@app.route('/generate', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = Image.open(BytesIO(base64.b64decode(request.json)))
        img.show()
        #img = base64_to_pil(request.json)

    return None















'''
@app.route('/generate', methods=['POST'])
def generate():  # put application's code here
    return 'Hello World!'
'''

if __name__ == '__main__':
    app.run(port=8080, debug = True)
