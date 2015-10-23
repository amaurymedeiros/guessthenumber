from random import shuffle

from flask import render_template, request

from . import app, xor, MASK

secret_number = 0
guesses = []

@app.route("/")
def home():
    _set_secret_number()
    return render_template('index.html', secret=secret_number)

@app.route('/guess_number', methods=['POST'])
def guess_number():
    secret = int(request.form.get('encrypted')) ^ MASK
    guess = int(request.form.get('guess'))
    return ""

def _set_secret_number():
    global secret_number
    secret_number = _get_random_number()

def _get_random_number():
    numbers = list('1234567890')
    shuffle(numbers)
    return int(''.join(numbers[:4]))