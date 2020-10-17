# Models database
from flask_sqlalchemy import SQLAlchemy
from .config import app

import datetime

db = SQLAlchemy(app)

class Clain(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(6), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer = db.relationship('Answer', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Clain %r>' % self.name

class Answer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con
