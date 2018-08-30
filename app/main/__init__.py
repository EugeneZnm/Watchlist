# import Blueprint class from flask
from flask import Blueprint

# initialise Blueprint class and pass in name of blueprint and _name_ to find the location of blueprint
main = Blueprint('main', __name__)

# import views and error modules to avoid circular dependencies
from . import views, error

