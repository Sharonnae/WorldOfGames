from flask import Flask, make_response, render_template
from werkzeug.exceptions import HTTPException
from Score import read_score
from utils import BAD_RETURN_CODE

app = Flask("WOG")


@app.route('/')
def my_func():
    return "Hello and welcome to the World Of Games"


@app.route('/game_score', methods=['GET'])
def game_score():
    score = read_score()
    return f'<html><head><title>Scores Game</title></head>' \
           f'<body><h1>The score is: <div id="score">{score}</div></h1></body></html>'


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e
    # now you're handling non-HTTP exceptions only
    return render_template(f'<html><head><title>Scores Game</title></head>' \
           f'<body><h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1></body></html>', e=e), 500


app.run(host="0.0.0.0", port=5001, debug=True)