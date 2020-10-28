# Configuracion del motor de la base de datos
# from flask import Flask
# from flask_mail import Mail
# from flask_login import LoginManager

class Config:
    SECRET_KEY = "b'_5#y2LF4Q8z\n\xec]/"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_DEFAULT_SENDER = 'central.salas@gmail.com'
    MAIL_USERNAME = 'central.salas@gmail.com'
    MAIL_PASSWORD = '12345admin'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

