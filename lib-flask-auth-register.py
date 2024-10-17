from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# *****************************************************************************
# Basic User Registration:
# Take the information user has inputted in register.html form and create a new 
# User object with email, name and password to save into the users.db.
#
# NOTE 1: Once the user is registered, we send them straight to the 
#         auth-secrets.html page.
# NOTE 2: In secrets.html page, the anchor tag makes a GET request to 
#         the server at the path /download to process downloading a file. That
#         path uses send_from_directory() call to process downloading the file.
# NOTE 3: This is basic Level 1 authentication. The user info  is in the db
#         but it is all (including pwds) in plain text.
# *****************************************************************************

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("auth-index.html")


# @app.route('/register')
# def register():
#     return render_template("auth-register.html")
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=request.form.get('password')
        )

        db.session.add(new_user)
        db.session.commit()

        # Passing over the user's name
        return render_template("auth-secrets.html", name=request.form.get('name'))

    return render_template("auth-register.html")


@app.route('/login')
def login():
    return render_template("auth-login.html")


@app.route('/secrets')
def secrets():
    return render_template("auth-secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    # specifying as_attachment parameter allows sending as attachment - sheet will open in the downloads folder.
    return send_from_directory('static', path="files/cheat_sheet.pdf") # , as_attachment=True


if __name__ == "__main__":
    app.run(debug=True)
