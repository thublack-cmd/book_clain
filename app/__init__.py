# Import from flask
from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager

from .config import Config
from .auth.auth_db import user_model
from .models import db
from .mail import mail
from .auth import auth
from .cubatta import cubatta
from .tribeca import tribeca
from .montreal import montreal
from .kavari import kavari
from .siete import siete
from .magia import magia
from .cassino import cassino


login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(auth)
    app.register_blueprint(cubatta)
    app.register_blueprint(tribeca)
    app.register_blueprint(montreal)
    app.register_blueprint(kavari)
    app.register_blueprint(siete)
    app.register_blueprint(magia)
    app.register_blueprint(cassino)

    login_manager.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    return app


@login_manager.user_loader
def load_user(username):
    return user_model.query(username)

