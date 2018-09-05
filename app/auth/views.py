from flask import render_template, redirect, request, url_for, flash
from . import auth
from .. import db
from ..models import User
from .forms import LoginForm, RegistrationForm

# importation of mail_message function
from .. email import mail_message
from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    """
    create instance of Loginform and pass it into login.html template
    """
    if login_form.validate_on_submit():
        """
        check if form is validated
        user is searched for in the database with the email received from form
        """
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            """
            use verify password method to confirm password entered matches with password hash stored in database
            """
            login_user(user, login_form.remember.data)
            """
            login function records the user as logged for current session if password ans hash match
            user object taken and form data remembered
            long time coolie is set if true
            """
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "watchlist login"
    return render_template('auth/login.html', login_form=login_form, title=title)


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        """
        new user is created from user model when form is submitted
        email, username and password are passed in
        """
        db.session.add(user)
        """
        new user is added to session
        
        """
        db.session.commit()
        """
        new user committed to session
        
        """
        title = 'New Account'

        mail_message("Welcome to Watchlist", "email/welcome_user", user.email, user=user)
        """
        call mail message
        pass in subject and template file where message body will be stored
        pass in new user's email address obtained from the registration form
        pass in user as a keyword argument
        """
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', registration_form=form)


# authenticated logout route calling logout_user function
@auth.route('/logout')
@login_required
def logout():
    """
    logout function that logs out user from application
    :return:
    """
    logout_user()
    # redirection to index page
    return redirect(url_for("main.index"))
