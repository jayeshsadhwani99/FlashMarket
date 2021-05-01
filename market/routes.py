# Imports required to add routes
from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db


# Index page
@app.route('/')
@app.route('/home')  # This will also redirect to index
def index():
    return render_template('home.html')


# Market Page
@app.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html', items=items)


# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market'))
    if form.errors != {}:  # If there are mo errors from validations
        for err_msg in form.errors.values():
            flash(
                f'There was an error while creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
