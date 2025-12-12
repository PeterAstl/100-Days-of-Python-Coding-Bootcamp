from flask import Flask

FLASK_APP = Flask(__name__)

@FLASK_APP.route('/')
def home():
    return '<h1>Hello World!</h1>'