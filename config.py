import os
class Config:
    '''
    General configuration parent class
    '''
    BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    HEAD_API_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}