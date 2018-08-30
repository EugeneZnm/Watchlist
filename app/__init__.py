from flask import Flask

# from config import DevConfig

from flask_bootstrap import Bootstrap

# importing config options
from config import config_options

bootstrap = Bootstrap()

# application factory function - used to test application under different configurations
# create app function taking configuration setting key as an argument
def create_app(config_name):
    app = Flask(__name__)

    # creating/ importing app configurations using from_object method
    app.config.from_object(config_options[config_name])

    # initialising flask extensions
    # init_app completes extension initialisation
    bootstrap.init_app(app)

    # Registering the blueprint
    # import instance created
    from .main import main as main_blueprint
    # call register_blueprint() method and pass in blueprint
    app.register_blueprint(main_blueprint)

    # setting / import configure_request() function from request.py file
    from .request import configure_request
    # call function and pass app instance
    configure_request(app)

    # add views and forms

    return app
