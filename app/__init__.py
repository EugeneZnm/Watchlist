from flask import Flask

from .config import  DevConfig

# intitalising application
app = Flask(__name__)


# setting up configuration
app.config.from_object(DevConfig)
# importing views form app folder

from app import views

