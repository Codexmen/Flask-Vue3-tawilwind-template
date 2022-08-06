from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import app_config

db = SQLAlchemy()
app = None

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    login = LoginManager(app)
    from app.models import User

    @login.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User}

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app
