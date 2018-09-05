# importation of blueprint
from flask import Blueprint

# creating Blueprint instance
auth = Blueprint('auth',__name__)

# import views module
from . import views, forms