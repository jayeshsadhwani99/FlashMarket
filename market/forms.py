# Imports required to create a form
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


# Creating a register form
class RegisterForm(FlaskForm):
    # Function to validate if username already exists
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username Taken. Try a different one')

    # Function to validate if email already exists
    def validate_email_address(self, email_to_check):
        email_address = User.query.filter_by(
            email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('Email already in use. Try a different one')

    # Fields in a form
    username = StringField(label='User Name', validators=[
                           Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[
                                Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[
                              Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[
                              EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


# Creating a login form
class LoginForm(FlaskForm):
    # Fields in a form
    username = StringField(label='User Name: ', validators=[DataRequired()])
    password = PasswordField(label='Passsword: ', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')


# Creating a form for purchasing items
class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')


# Creating a form for selling items
class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')
