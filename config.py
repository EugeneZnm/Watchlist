# import os module allowing interaction with operating system dependent functionality
import os


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
