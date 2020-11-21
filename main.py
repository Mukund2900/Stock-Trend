import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib 
app = Flask(__name__)
model = joblib.load("abc.pkl")
@app.route('/')
def home():
    return render_template('abc.html')


@app.route('/', methods = ['POST'])
def stocks():
    if(request.method == 'POST') : 
        term = str(model.info())


    return render_template('abc.html', your_term = term)



if __name__ == "__main__":
    app.run(debug=True)