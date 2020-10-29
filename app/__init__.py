# Import from flask
from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .models import user_model
from .models import db
from .mail import mail


login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    return app


@login_manager.user_loader
def load_user(username):
    return user_model.query(username)
