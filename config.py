# import os module allowing interaction with operating system dependent functionality
import os
# setup smtp server and configurations to connect to smtp server port
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = '587'
MAIL_USE_TLS =True # enables transport layer security to secure emails when sending emails

# emails and password to authenticate the gmail smtp server and are set as environment variables
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class Config:
    """
    General configuration parent class

    contains configuration used in both production and development stages
    """

    ## os.environ.get() used to get movie_api_key and secret key
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')

    # enable CSRF secret key
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://eugene:necromancer@localhost/watchlist'

    # configuration UPLOAD_PHOTOS_DEST created specifying destination of image storage, a photos folder in static folder
    # photos should be stored in app instead of inside database
    # the path to the photos is stored in the database
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


class ProdConfig(Config):
    """
    Production Configuration child class

     Contains configurations used in  production stage and inherits from parent Config class
    args:
        Config: The parent configuration class with General congfiguration
    """
    pass


class DevConfig(Config):
    """
    Development configuration child class

    Contains configurations used in development stages of application and inherits from parent Config class

    """

    # enabling debug mode
    DEBUG = True


# dictionary config options used to access different configuration option classes
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
