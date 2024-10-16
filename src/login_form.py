from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), validators.Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label="Log In")
