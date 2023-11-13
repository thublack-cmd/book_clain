# Import from flask
from flask import Flask

from .config import Config
# from .auth.auth_db import user_model
from .models import db
# from .auth import auth
from .ludopatia import ludopatia
from .ludopatia.cubatta import ludopatia_cub

# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # app.register_blueprint(auth)
    app.register_blueprint(ludopatia)
    app.register_blueprint(ludopatia_cub)

    # login_manager.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

# @login_manager.user_loader
# def load_user(username):
#     return user_model.query(username)

