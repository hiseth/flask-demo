import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TESTING = False
    FLASK_ENV = 'development'
    DEBUG = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', default='A very terrible secret key')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, '/dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


config_type = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
