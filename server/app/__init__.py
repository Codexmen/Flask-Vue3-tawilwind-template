from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask import Flask
from .config import app_config


db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    from .api.utils.auth import auth_bp
    app.register_blueprint(auth_bp)
    login_manager.init_app(app)


    @app.route('/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
