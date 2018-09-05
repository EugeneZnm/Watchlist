from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# import uploadset class defining type of file being uploaded
from flask_uploads import UploadSet, configure_uploads, IMAGES
# creating instance of class login
login_manager = LoginManager()

# login_manager.session_protection attribute provides different security levels
# monitors changes in user request header and logs the user out
login_manager.session_protection = 'strong'

# endpoint prefixed with blueprint name auth because it is located inside a blueprint
login_manager.login_view = 'auth.login'

from flask import Flask
# from config import DevConfig

from flask_bootstrap import Bootstrap

# importing config options
from config import config_options

# import Mail class from flask_mail extension
from flask_mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()

photos = UploadSet('photos', IMAGES)

mail = Mail()
# application factory function - used to test application under different configurations
# create app function taking configuration setting key as an argument

def create_app(config_name):
    app = Flask(__name__)

    # creating/ importing app configurations using from_object method
    app.config.from_object(config_options[config_name])

    # initialising flask extensions
    # init_app completes extension initialisation
    bootstrap.init_app(app)
    # call init app method and pass in app instance
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    # import instance created
    from .main import main as main_blueprint
    # call register_blueprint() method and pass in blueprint
    app.register_blueprint(main_blueprint)

    # setting / import configure_request() function from request.py file
    from .request import configure_request
    # call function and pass app instance
    configure_request(app)

    # configure Uploadset
    configure_uploads(app, photos)
    """
    configure uploads function  passing in app instance
    """
    from .auth import auth as auth_blueprint
    # registering blueprint instance in create_app function
    # url_prefix argument adding prefix to all routes registered with specific blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
    # add views and forms

    # initialise flask_mail extension
    mail.init_app(app)

    return app
