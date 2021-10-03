import os
import csv
import json
import requests 

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename

from google.cloud import vision

# Some utilites
import numpy as np

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


## url 

@app.route('/generation', methods=['POST', 'GET'])
def generation():
    if request.method == 'POST':
        url = request.form['input']
            
        # Instantiates a client
        client = vision.ImageAnnotatorClient()
        image = vision.Image()
        image.source.image_uri = url

        # Performs label detection on the image file    
        response = client.label_detection(image=image)
        labels = response.label_annotations     
    
        if response.error.message: return 'Error: Image not found.'
        else: d = {k : v for k, v in [[label.description, label.score] for label in labels][:3]}
                 
        tags = ' '.join(d.keys())
        
        poem="hello world"
        
        return render_template('index.html', tags=f'Image tags: {tags}', poem=poem)
    
    else:
        return '404'
    
        



















'''
@app.route('/generate', methods=['POST'])
def generate():  # put application's code here
    return 'Hello World!'
'''

if __name__ == '__main__':
    app.run(port=8080, debug = True)
