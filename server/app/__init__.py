from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

from .config import app_config

db = SQLAlchemy()
app = None


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    CORS(app, resources={"/api/*": {"origins": "http://localhost:8080"}}, supports_credentials=True)
    app.config.from_pyfile('config.py')
    app.config['SESSION_COOKIE_SAMESITE'] = "None"
    app.config['SESSION_COOKIE_SECURE'] = True
    db.init_app(app)
    migrate = Migrate(app, db)
    login = LoginManager(app)
    from .api import auth
    from .models import User, UserStock, Ticker

    app.register_blueprint(auth.bp)
    @login.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.User.query.get(int(user_id))

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'UserStock': UserStock, 'Ticker': Ticker}

    return app
