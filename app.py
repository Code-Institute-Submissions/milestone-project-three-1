import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for, flash

app = Flask(__name__)
app.secret_key = "qwer1234"


def get_question(number):
    
    """ Use current turn number with array of odd numbers to determine which line the next question is on"""
    questions_index = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    current_question = questions_index[number-1]
    
    riddles = open("static/riddles.txt", "r")
    
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
    
    if request.method == "POST":
        
        if session["current_question_number"] < 10:
            
            session["current_question_number"] +=1
            
        else:
        
            return redirect('gameover')
            
    question_id = session["current_question_number"]
    
    return redirect(url_for('question', question_id=question_id))

@app.route('/question/<int:question_id>', methods = ["GET", "POST"])    
def question(question_id):
    
    if question_id != session["current_question_number"]:
        return redirect('cheaters')
    
    question = get_question(question_id)
    
    return render_template('questions.html', question=question)

@app.route('/gameover')
def gameover():
 
    username = session["username"]
    correct_answers = session["current_question_number"]
    
    ## Answer number doesn't increment on final correct answer, 
    ## so score adjestment needed on all but last
    if correct_answers < 10:
        correct_answers -= 1
        
    score = correct_answers*10
    date = datetime.today().strftime('%x')
    
    with open('static/scoreboard.txt', 'a') as scoreboard:
        
        scoreboard.write('{}, {}, {}'.format(username, score, date))
        scoreboard.write('\n')
    
    session.clear()
    
    return redirect(url_for('scoreboard'))
    
@app.route('/scoreboard')
def scoreboard():
    
    scoreboard = open("static/scoreboard.txt", "r")
    scores = []
    
    for score in scoreboard:

        score_list = score.split(',')
        scores.append(score_list)
    
    return render_template('scoreboard.html', scores=scores)
    
@app.route('/reset')
def reset():
    
    session.clear()
    
    return redirect(url_for('index'))
    

@app.route('/cheaters')
def cheaters():
    
    username = session["username"]
    score = "CHEATER"
    date = datetime.today().strftime('%x')
    
    with open('static/scoreboard.txt', 'a') as scoreboard:
        
        scoreboard.write('{}, {}, {}'.format(username, score, date))
        scoreboard.write('\n')
    
    session.clear()
    
    return redirect(url_for('scoreboard'))
    
    
if __name__ == "__main__":
    app.run(host=os.getenv('IP', "0.0.0.0"), port=int(os.getenv('PORT', "5000")), debug=False)