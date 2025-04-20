import os

class Config:
    """Base configuration settings."""

    API_KEY = os.getenv('PREDICTION_API_KEY')
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USER = os.getenv('MYSQL_USER')
    DB_PASSWORD = os.getenv('MYSQL_PASSWORD')
    DB_NAME = 'tennis'

    MODEL_PATH = 'data/models/xgboost_tennis_model.ubj'

    LOG_LEVEL = 'INFO'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}

config_name = 'dev'
app_config = config_by_name.get(config_name, DevelopmentConfig)()
