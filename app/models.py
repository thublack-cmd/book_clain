# Models database
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


import datetime

db = SQLAlchemy()

class Clain_cub(db.Model):

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

class Answer_cub(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con


class Clain_tri(db.Model):

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

class Answer_tri(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con


class Clain_mon(db.Model):

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
 
class Answer_mon(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con


class Clain_kav(db.Model):

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

class Answer_kav(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con


class Clain_sie(db.Model):

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

class Answer_sie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con


class Clain_mag(db.Model):

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

class Answer_mag(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con


class Clain_cas(db.Model):

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

class Answer_cas(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con


class User(db.Model):

    username = db.Column(db.String(15), nullable=False, primary_key=True)
    password = db.Column(db.String(150), nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=True, default=False)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<User {self.last_name}, {self.first_name}>'


def get_user(user_id):
    return User.query.get(user_id)


class user_data:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class user_model(UserMixin):
    def __init__(self, data_user):
        self.id = data_user.username
        self.password = data_user.password

    @staticmethod
    def query(user_id):
        user = get_user(user_id)
        data_user = user_data(
                username = user.username,
                password = user.password,
                )
        return user_model(data_user)
