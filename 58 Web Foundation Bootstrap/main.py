from flask import Flask, render_template

FLASK_APP = Flask(__name__)

@FLASK_APP.route('/')
def home():
    return render_template("website.html")

if __name__ == '__main__':
    FLASK_APP.run()