import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from setting import config_type


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_type[os.getenv('FLASK_ENV', 'dev')])
    register_extensins(app)
    register_blueprint(app)

    return app


def register_blueprint(app):
    pass


def register_extensins(app):
    pass
