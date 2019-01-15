import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "qwer1234"
lives = 3
question = 0

def test_func():
    
    return 2

@app.route('/', methods = ["GET", "POST"])
def index():
    
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["question"] = 1
        
    if "username" in session:
        return redirect(url_for("questions", username = session["username"]))
    
    return render_template('index.html')
    
@app.route('/questions/<username>', methods = ["GET", "POST"])    
def questions(username):

    if request.method == "POST":
        username = session["username"]
        
        return redirect(url_for("questions", username = session["username"]))
        
    return render_template('questions.html', username = username)
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=True)