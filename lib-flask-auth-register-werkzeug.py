from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# *****************************************************************************
# User Registration with Hashed and Salted Passwords using Werkzeug:
# The program builds on the lib-flask-auth-register.py to store hashed and
# salted passwords in the DB rather than plain text.
#
# NOTE 1: /register route code is modified to call the Werkbeug helper function 
#          generate_password_hash()
# NOTE 2: Doc hash and salt the user's password at: 
#         https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security.
#         Hashing Algorithm: pbkdf2:sha256
#         salt_length: 8 # this is the length to store the number of iterations
# NOTE 3: The salt is stored within the hash itself. It’s not stored as a 
#         separate field in the database. When you generate a password hash 
#         using Werkzeug, the resulting string includes the salt, the algorithm 
#         used, the number of iterations, and the final hash—all concatenated 
#         in a specific format. Example:
# pbkdf2:sha256$260000$vnEE5ZODmjK9EqxM$1b3c10fe2d66071de06c1a60cd9f6ab404500d15f0a4d302c2c05bc30e9f5e74
#         1. Algorithm: pbkdf2:sha256
#         2. Iterations: 260000 (the number of hash iterations)
#         3. Salt: vnEE5ZODmjK9EqxM
#         4. Hash: 1b3c10fe2d66071de06c1a60cd9f6ab404500d15f0a4d302c2c05bc30e9f5e74
# NOTE 4: When you call werkzeug.security.check_password_hash, Werkzeug parses 
#         the stored hash string, extracts the salt and other parameters, and 
#         then uses them to hash the input password. If the resulting hash 
#         matches the stored hash, the password is correct.
# NOTE 5: Salt Rounds are used in bcrypt algorithm instead of iterations. 
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


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Hashing and salting the password entered by the user 
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        # Storing the hashed password in our database
        new_user = User(
            email=request.form.get('email'),
            name=request.form.get('name'),
            password=hash_and_salted_password,
        )

        db.session.add(new_user)
        db.session.commit()

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
