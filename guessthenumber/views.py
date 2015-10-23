from flask import jsonify, render_template, request

from . import app, xor
from utils import calculate_score, get_random_number

secret_number = 0
guesses = []

@app.route("/")
def home():
    _set_secret_number()
    return render_template('index.html', secret=secret_number)

@app.route('/guess_number', methods=['POST'])
def guess_number():
    secret = xor(int(request.form.get('encrypted')))
    guess = int(request.form.get('guess'))
    return jsonify(calculate_score(secret, guess))

def _set_secret_number():
    global secret_number
    secret_number = get_random_number()
