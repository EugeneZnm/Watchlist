from flask import Flask

from .config import  DevConfig

from flask_bootstrap import Bootstrap

from app import views

from app import error

# intitalising application
# passing in instance_relative_config allowing connection to instance folder when app instance is created
app = Flask(__name__, instance_relative_config=True)


# setting up configuration
app.config.from_object(DevConfig)

# connecting to config.py file and its contents
app.config.from_pyfile('config.py')

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
# importing views form app folder

from app import views

