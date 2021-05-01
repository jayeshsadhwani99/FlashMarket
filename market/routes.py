# Imports required to add routes
from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user


# Index page
@app.route('/')
@app.route('/home')  # This will also redirect to index
def index():
    return render_template('home.html')


# Market Page
@app.route('/market', methods=['GET', 'POST'])
@login_required
def market():
    purchase_form = PurchaseItemForm()
    # If the method is POST
    if request.method == 'POST':
        # Get item name from form
        purchased_item = request.form.get('purchased_item')
        # Find item in Database
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        # Check if there exists such an object
        if p_item_object:
            # Only if user can purchase
            if current_user.can_purchase(p_item_object):
                # Call a function to set ownership of item
                p_item_object.setOwnership(current_user)
                flash(
                    f'Congratulations! You just purchased {p_item_object.name} for ₹{p_item_object.price}', category='success')
            else:
                flash(
                    f'Sorry! your budget is not enough to purchase {p_item_object.name}', category='danger')

        return redirect(url_for('market'))

    # If the request is GET
    if request.method == 'GET':
        # Only show items that have no owners
        items = Item.query.filter_by(owner=None)
        return render_template('market.html', items=items, purchase_form=purchase_form)


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

        # Login user when created
        login_user(user_to_create)
        flash(
            f'Account created successfully. Now logged in as: {user_to_create.username}', category='success')
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
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(
                f'Success. You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market'))
        else:
            flash('Username and Passwords do not match. Try Again',
                  category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('index'))
