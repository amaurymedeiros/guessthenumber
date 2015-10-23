from flask import Flask

MASK = 3039

def xor(number):
    return number ^ MASK

app = Flask(__name__)

app.jinja_env.globals.update(xor=xor)