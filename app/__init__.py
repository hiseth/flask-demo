import os
from flask import Flask
from setting import config_type
from setting import BASE_DIR
from .models import User


def create_app():
    app = Flask(__name__, template_folder=os.path.join(BASE_DIR, 'templates'))
    app.config.from_object(config_type[os.getenv('FLASK_ENV', 'dev')])

    register_extension(app)
    register_blueprint(app)

    return app


def register_blueprint(app):
    from app.main import main as main_blueprint
    from app.auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)


def register_extension(app):
    from app.extension import db
    from app.extension import login_manage

    db.init_app(app)
    login_manage.login_view = 'auth.login'
    login_manage.init_app(app)

    @login_manage.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
