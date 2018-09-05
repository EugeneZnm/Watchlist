from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    """
    registration form class
    """
    # input field created for users
    email = StringField('Your Email Address', validators=[Required(), Email()])
    """
    input field created for user email address passing in required and and email validators
    
    """
    username = StringField('Enter your username', validators=[Required()])
    """
    username field with 
    """
    password = PasswordField('Password',
                             validators=[Required(), EqualTo('password_confirm', message='Passwords must match')])
    """
    password validator form with EqualTo validator to password making sure both passwords are the same before form is submitted
    """
    password_confirm = PasswordField('Confirm Passwords', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        """
        method taking in data field,  checks database to confirm there's no user registered with email address
        a ValidateError is raised when user with similar email is found and error message passed is displayed
        no form submitted
        :param data_field:
        :return:
        """
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
        """
        checks to see if username is unique
        ValidateError is raised when username with similar name is found
        :param data_field:
        :return:
        """
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
