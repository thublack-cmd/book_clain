# from Flask
from flask import render_template
# from flask_sqlalchemy import SQLAlchemy

from app.models import db, Personas
from app.config import app

# from Python
from datetime import date

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)

now = (date.today()).strftime('%d-%m-%Y')

@app.route('/')
def client_view():
    return render_template('cliente.html', dia=now)

db.create_all()
