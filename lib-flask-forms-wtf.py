from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

# *****************************************************************************
# One of the biggest reasons why we would choose WTForms over HTML Forms is the 
# built-in validation. Instead of us having to write our own validation code 
# e.g. emails should contain a "@" and a "." to be valid or make sure that 
# passwords are minimum of 8 characters, we can use all these validation rules 
# straight out of the box from WTForms.
# *****************************************************************************

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()]) # EmailField requires email_validator - see requirements.txt
    password = PasswordField(label='Password', validators=[DataRequired()]) # PasswordField obscures the text typed in with *'s
    submit = SubmitField(label="Log In") # this is in place of the submit input/button.


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret" # for CSRF protection. Please see {‌{ form.csrf_token }} used in html


@app.route("/")
def home():
    return render_template("wtf-forms-index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit(): # it will be false, if it is a GET request. Alternative is using requests.method=="POST"
        # To get form data, we access the form-field's data attribe as <form_object>.<form_field>.data
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("wtf-forms-login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
