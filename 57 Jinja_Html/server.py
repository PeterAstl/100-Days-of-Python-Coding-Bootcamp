
from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.date.today().year
    return render_template('index1.html', random_number=random_number, current_year=current_year)


if __name__ == '__main__':
    app.run(debug=True)