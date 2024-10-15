from flask import Flask, render_template
from random import randint
from datetime import date

app = Flask(__name__)


@app.route('/')
def home():
    choice = randint(1, 10)
    year = date.today().year
    name = "John Konnayil Vincent"
    return render_template("jinja-intro.html", num=choice, current_year=year, author=name)


if __name__ == "__main__":
    app.run(debug=True)
