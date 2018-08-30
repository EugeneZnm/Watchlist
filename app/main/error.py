# import render template and flask application instance
from flask import render_template

from . import main


# decorator passing in error we receive
# import blueprint instance main and use it to define decorator
@main.app_errorhandler(404)
# view function returning fourOwfour.html
def four_Ow_four(error):
    """
    Function to render 404 page
    :param error:
    :return:
    """

    return render_template('fourOwfour.html'), 404
