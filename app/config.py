# Configuracion del motor de la base de datos
from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = "b'_5#y2LF4Q8z\n\xec]/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_DEFAULT_SENDER'] = 'central.salas@gmail.com'
app.config['MAIL_USERNAME'] = 'central.salas@gmail.com'
app.config['MAIL_PASSWORD'] = '12345admin'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
login_manager = LoginManager(app)
