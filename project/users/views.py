from flask import request, flash, redirect, url_for, Blueprint, render_template
from flask_login import login_required, login_user, logout_user, current_user
from sqlalchemy import desc

from project.users.forms import RegistrationForm, LoginForm  # relative import
from project.users.models import *  # relative import
from project.extensions import db, login_manager  # relative import


users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


@users_blueprint.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # Register form is valid, check if username already in db
        # if form.username.data in [row[0] for row in db.session.query(RegisteredUser.username).all()]:
        #     error = 'This username exists!'
        #     return render_template('signup.html', form=form, error=error)

        # Add a new user, the user id is the current max(user.id) + 1
        try:
            cur_max_id = db.session.query(RegisteredUser.id).order_by(desc(RegisteredUser.id)).all()[0][0]
        except IndexError:  # If it's an empty table
            cur_max_id = 0

        db.session.add(RegisteredUser(
            cur_max_id + 1, form.username.data, form.password.data, form.email.data))
        db.session.commit()
        flash('Thanks for signing up')
        return redirect(url_for('home.home'))

    return render_template('signup.html', form=form, error=form.errors)


@users_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('home.home'))

    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('Login successful!')
            return redirect(url_for('home.home'))
        else:
            error = "User doesn't exist or password incorrect"

    return render_template('login.html', form=form, error=error)


@users_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))


@login_manager.user_loader
def load_user(user_id):
    return RegisteredUser.query.filter_by(id=user_id).first()
