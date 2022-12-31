# Import from flask
from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager

from .config import Config
from .auth.auth_db import user_model
from .models import db
from .mail import mail
from .auth import auth
from .encuestas.cubatta import ecubatta
from .sala.cubatta import cubatta
from .sala.tribeca import tribeca
from .sala.montreal import montreal
from .sala.kavari import kavari
from .sala.siete import siete
from .sala.magia import magia
from .sala.cassino import cassino
from .uchukuta.zarate import zarate
from .uchukuta.proceres import proceres
from .uchukuta.huacho import huacho
from .uchukuta.huarmey import huarmey
from .uchukuta.casma import casma
from .ludopatia import ludopatia
from .ludopatia.cubatta import ludopatia_cub
from .publicidad import publicidad


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
    app.register_blueprint(zarate)
    app.register_blueprint(proceres)
    app.register_blueprint(huacho)
    app.register_blueprint(huarmey)
    app.register_blueprint(casma)
    app.register_blueprint(ecubatta)
    app.register_blueprint(ludopatia)
    app.register_blueprint(ludopatia_cub)
    app.register_blueprint(publicidad)

    login_manager.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    return app


@login_manager.user_loader
def load_user(username):
    return user_model.query(username)

