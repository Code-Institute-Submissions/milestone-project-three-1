import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for, flash

app = Flask(__name__)
app.secret_key = "qwer1234"



def get_question(number):
    
    """ Use current turn number with array of odd numbers to determine which line the next question is on"""
    questions_index = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    current_question = questions_index[number-1]
    
    riddles = open("riddles.txt", "r")
    
    counter = 1
        
    while counter < current_question:
        riddles.readline();
        counter += 1

    current_question = {"question" : riddles.readline().rstrip(), "answer" : riddles.readline().rstrip()}
    
    riddles.close()
    
    return current_question

@app.route('/', methods = ["GET", "POST"])
def index():
    
    if request.method == "POST":
        
        session["username"] = request.form["username"]
        session["score"] = 0
        session["lives"] = 3
        session["current_question_number"] = 1
        
    if "username" in session:
        return redirect(url_for("questions"))
    
    return render_template('index.html')
    
@app.route('/questions', methods = ["GET", "POST"])    
def questions():
    
    if "username" not in session:
        return redirect(url_for("index"))
        
    question = get_question(session["current_question_number"])
    
    if request.method == "POST":
        
        if session["current_question_number"] < 10:
            
            session["current_question_number"] +=1
            question = get_question(session["current_question_number"])
            
        else:
        
            return render_template('success.html')
        
        flash('Correct!')
        return render_template('questions.html', user=session["username"], question=question)
    
    return render_template('questions.html', user=session["username"], question=question)

@app.route('/reset')
def reset():
    
    session.clear()
    
    return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=True)