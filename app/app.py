import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('../model/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('templates/index.html')

@app.route('/about')
def about():
    return render_template('templates/about.html')

@app.route('/who')
def who():
    return render_template('templates/who.html')

@app.route('/generate', methods=['POST'])
def generate():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug = True)
