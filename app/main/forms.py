# import class FlaskForm from flask_wtf module helping create a Form Class
from flask_wtf import FlaskForm

# import StringField TextAreaField and SubmitField classes aiding in creation of textfield, text Area field and submit button
from wtforms import StringField, TextAreaField, SubmitField

# import required class validator preventing user from submitting form without inputting a value
from wtforms.validators import Required


# create ReviewForm class inheriting from FlaskForm class
class ReviewForm(FlaskForm):

    # initialising field types by passing in two parameters 1: Label 2: list of validators where required validator is initialised
    title =StringField('Review title', validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit =SubmitField('Submit')


class UpdateProfile(FlaskForm):
    """
    form class update profile
    """
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')