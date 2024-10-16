from flask_bootstrap import Bootstrap5
from flask import Flask, render_template
from src.login_form import LoginForm

app = Flask(__name__)
bootstrap = Bootstrap5(app)
# From Flask Doc: A secret key that will be used for securely signing the session cookie
# and can be used for any other security related needs by extensions or your
# application. It should be a long random bytes or str.
app.secret_key = "John Konnayil Vincent"

VALID_EMAIL = "admin@email.com"
VALID_PASSWORD = "12345678"


@app.route("/")
def home():
    return render_template('bootstrap-index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == VALID_EMAIL and login_form.password.data == VALID_PASSWORD:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('bootstrap-login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
