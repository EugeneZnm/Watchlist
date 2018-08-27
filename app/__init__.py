from flask import Flask

from app import app

# intitalising application
app = Flask(__name__)

# importing views form app folder

from app import views

#views
@app.route('/')
def index():