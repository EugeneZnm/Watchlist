class Config:
    """
    General configuration parent class

    contains configuration used in both production and development stages
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'


class Production(Config):
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

