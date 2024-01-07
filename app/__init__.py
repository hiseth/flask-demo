import os
from flask import Flask
from setting import config_type
from setting import BASE_DIR


def create_app():
    app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))
    app.config.from_object(config_type[os.getenv('FLASK_ENV', 'dev')])

    register_extensins(app)
    register_blueprint(app)

    return app


def register_blueprint(app):
    from app.main import main as main_blueprint
    from app.auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)


def register_extensins(app):
    from app.extension import db
    db.init_app(app)
