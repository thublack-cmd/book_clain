# Configuracion del motor de la base de datos
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
