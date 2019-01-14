import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "qwer1234"

@app.route('/', methods = ["GET", "POST"])
def index():
    
    if request.method == "POST":
        
        session["username"] = request.form["username"]
        
        return render_template('questions.html', username = session["username"])
    
    return render_template('index.html')
    
@app.route('/questions', methods = ["GET", "POST"])    
def questions():

    return render_template('index.html')
    
app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=True)