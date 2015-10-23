from flask import jsonify, render_template, request

from . import app, xor
from utils import calculate_score, get_random_number

@app.route("/")
def home():
    return render_template('index.html', secret=get_random_number())

@app.route('/guess_number', methods=['POST'])
def guess_number():
    secret = xor(int(request.form.get('encrypted')))
    guess = int(request.form.get('guess'))
    return jsonify(calculate_score(secret, guess))

