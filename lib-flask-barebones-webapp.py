from flask import Flask
from random import randint


# Animated GIFs below are from giphy.com, a public repository
GAME_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH_GIF = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW_GIF = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT_GIF = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

app = Flask(__name__)


def style_homepage(fn):
    def wrapper():
        return "<h1>" + fn() + f"</h1><img src={GAME_GIF}>"
    return wrapper


@app.route('/')
@style_homepage
def home_page():
    return "Guess a number between 0 and 9"


@app.route('/<int:guess>')
def guess_page(guess):
    if home_guess == guess:
        return f"<h1 style='color:green'>You found me!</h1><img src={CORRECT_GIF}>"
    elif home_guess > guess:
        return f"<h1 style='color:red'>Too low, try again!</h1><img src={LOW_GIF}>"
    else:
        return f"<h1 style='color:purple'>Too high, try again!</h1><img src={HIGH_GIF}>"


if __name__ == "__main__":
    home_guess = randint(0, 9)
    app.run(debug=True)
