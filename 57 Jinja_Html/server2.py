
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index3.html')


@app.route('/guess/<name>')
def guess(name):
    age_url = f"https://api.agify.io?name={name}"
    response = requests.get(age_url)
    age_data = response.json()
    age = age_data["age"]
    return render_template('index.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)