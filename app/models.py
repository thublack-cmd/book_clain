# Models database
from flask_sqlalchemy import SQLAlchemy
from models import app

db = SQLAlchemy(app)

class Personas(db.Model):
    __tablename__ = 'personas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=True)
