from flask import Flask
import random

app = Flask(__name__)


random_number = random.randint(0, 9)


@app.route('/')
def index():
    return '<h1>"Guess a number between 0 and 9"</h1>'

@app.route('/<int:guessed>')
def guess(guessed):
    if guessed < random_number:
        return f'<h1>{guessed} is too low</h1>'
    if guessed > random_number:
        return f'<h1>{guessed} is too high</h1>'
    else:
        return f'<h1>{guessed} is correct</h1>'

if __name__ == '__main__':
    app.run()
