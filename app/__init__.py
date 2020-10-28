# Import from flask
from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager

from .config import Config
from .models import user_model
from .models import db
from .mail import mail


login_manager = LoginManager()

@login_manager.user_loader
def load_user(username):
    return user_model.query(username)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mail.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)

    return app
