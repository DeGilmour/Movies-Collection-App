from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=None):
    app = Flask(__name__)
    
    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
