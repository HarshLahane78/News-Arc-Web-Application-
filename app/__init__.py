# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config
import logging

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    setup_logging(app)

    from .routes import main
    app.register_blueprint(main)
    from .api import api
    app.register_blueprint(api, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app


def setup_logging(app):
    logging.basicConfig(level=app.config['LOGGING_LEVEL'])
    handler = logging.FileHandler('app.log')
    handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
    app.logger.addHandler(handler)
