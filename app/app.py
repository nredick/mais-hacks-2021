import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

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

'''
@app.route('/generate', methods=['POST'])
def generate():  # put application's code here
    return 'Hello World!'
'''

if __name__ == '__main__':
    app.run(port=8080, debug = True)
