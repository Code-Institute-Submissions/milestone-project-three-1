import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

APP = Flask(__name__)
APP.secret_key = "qwer1234"


def get_question(number):
    """ Use current turn number with array of odd
     numbers to determine which line the next question is on
     """
    questions_index = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    current_question = questions_index[number-1]

    riddles = open("static/riddles.txt", "r")

    counter = 1

    while counter < current_question:
        riddles.readline()
        counter += 1

    current_question = {"question": riddles.readline(
    ).rstrip(), "answer": riddles.readline().rstrip()}

    riddles.close()

    return current_question


@APP.route('/', methods=["GET", "POST"])
def index():
    """
    Base route, sets session variables for each user
    """
    if request.method == "POST":

        session["username"] = request.form["username"]
        session["score"] = 0
        session["lives"] = 3
        session["current_question_number"] = 1

    if "username" in session:
        return redirect(url_for("questions"))

    return render_template('index.html')


@APP.route('/questions', methods=["GET", "POST"])
def questions():
    """
    Questions route, tracks current question and redirects appropriately
    """
    if "username" not in session:
        return redirect(url_for("index"))

    if request.method == "POST":

        if session["current_question_number"] < 10:

            session["current_question_number"] += 1

        else:

            return redirect('gameover')

    question_id = session["current_question_number"]

    return redirect(url_for('question', question_id=question_id))


@APP.route('/question/<int:question_id>', methods=["GET", "POST"])
def question(question_id):
    """
    Indivdual question route, fetches current question and 
    watches for mismatch in id to indicate user is trying to cheat
    """
    if question_id != session["current_question_number"]:
        return redirect('cheaters')

    question = get_question(question_id)

    return render_template('questions.html', question=question)


@APP.route('/gameover')
def gameover():
    """
    Game over route, reached when user answered all ten questions,
    or when user got a question wrong and lost,
    determines score based on number of correct answers
    """
    username = session["username"]
    correct_answers = session["current_question_number"]

    # Answer number doesn't increment on final correct answer,
    # so score adjestment needed on all but last
    if correct_answers < 10:
        correct_answers -= 1

    score = correct_answers*10
    date = datetime.today().strftime('%x')

    with open('static/scoreboard.txt', 'a') as scoreboard:

        scoreboard.write('{}, {}, {}'.format(username, score, date))
        scoreboard.write('\n')

    session.clear()

    return redirect(url_for('scoreboard'))


@APP.route('/scoreboard')
def scoreboard():
    """
    Scoreboard route, displays scoreboard to users,
    doesn't require active session to view
    """
    scoreboard = open("static/scoreboard.txt", "r")
    scores = []

    for score in scoreboard:

        score_list = score.split(',')
        scores.append(score_list)

    return render_template('scoreboard.html', scores=scores)


@APP.route('/reset')
def reset():
    """
    Reset route, clears all session variables and sends user back to index
    """
    session.clear()

    return redirect(url_for('index'))


@APP.route('/cheaters')
def cheaters():
    """
    Cheaters route, saves the current username and sets their score to
    cheater flag, then appends data to the scoreboard file for all the world
    to see
    """
    username = session["username"]
    score = "CHEATER"
    date = datetime.today().strftime('%x')

    with open('static/scoreboard.txt', 'a') as scoreboard:

        scoreboard.write('{}, {}, {}'.format(username, score, date))
        scoreboard.write('\n')

    session.clear()

    return redirect(url_for('scoreboard'))


if __name__ == "__main__":
    APP.run(host=os.getenv('IP', "0.0.0.0"), port=int(
        os.getenv('PORT', "5000")), debug=True)
