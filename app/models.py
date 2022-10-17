# Models database
from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

class Clain_cub(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500))
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_cub = db.relationship('Answer_cub', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_cub.id'))
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
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_tri = db.relationship('Answer_tri', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_tri.id'))
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
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_mon = db.relationship('Answer_mon', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_mon.id'))
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
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_kav = db.relationship('Answer_kav', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_kav.id'))
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
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_sie = db.relationship('Answer_sie', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_sie.id'))
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
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_mag = db.relationship('Answer_mag', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_mag.id'))
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
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_cas = db.relationship('Answer_cas', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_cas.id'))
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

class Clain_uchu_zarate(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_uchu_zarate = db.relationship('Answer_uchu_zarate', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_uchu_zarate.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Clain %r>' % self.name

class Answer_uchu_zarate(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con

class Clain_uchu_proceres(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_uchu_proceres = db.relationship('Answer_uchu_proceres', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_uchu_proceres.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Clain %r>' % self.name

class Answer_uchu_proceres(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con

class Clain_uchu_huacho(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_uchu_huacho = db.relationship('Answer_uchu_huacho', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_uchu_huacho.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Clain %r>' % self.name

class Answer_uchu_huacho(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con

class Clain_uchu_huarmey(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_uchu_huarmey = db.relationship('Answer_uchu_huarmey', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_uchu_huarmey.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Clain %r>' % self.name

class Answer_uchu_huarmey(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con

class Clain_uchu_casma(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(12))
    name = db.Column(db.String(100), nullable=False)
    type_doc = db.Column(db.String(3), nullable=True)
    nro_doc = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500))
    date = db.Column(db.DateTime, nullable=False)
    type_claim = db.Column(db.String(7), nullable=False)
    amount = db.Column(db.Integer)
    detail = db.Column(db.String(500), nullable=False)
    answer_uchu_casma = db.relationship('Answer_uchu_casma', uselist=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer_uchu_casma.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Clain %r>' % self.name

class Answer_uchu_casma(db.Model):

    __bind_key__= 'uchukuta'
    id = db.Column(db.Integer, primary_key=True)
    answer_con = db.Column(db.String(500), nullable=False)
    id_user = db.Column(db.String(15))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    def __repr__(self):
        return '<Answer %r>' % self.answer_con

class Ludopatia_db(db.Model):

    __bind_key__= 'ludopatia'
    id = db.Column(db.Integer, primary_key=True)
    num_reg = db.Column(db.Integer, nullable=False)
    nro_dni = db.Column(db.String(15))
    name_dni = db.Column(db.String(100))

    def __repr__(self):
        return '<Cliente %r>' % self.nro_dni

class ingreso_cubatta(db.Model):

    __bind_key__= 'ludopatia'
    id = db.Column(db.Integer, primary_key=True)
    ingreso = db.Column(db.DateTime, default=datetime.datetime.now)
    nro_document = db.Column(db.String(15))
    is_ludo = db.Column(db.Integer)

    def __repr__(self):
        return '<Cliente %r>' % self.nro_document

class no_access(db.Model):

    __bind_key__= 'ludopatia'
    id = db.Column(db.Integer, primary_key=True)
    nro_dni = db.Column(db.String(15))
    name = db.Column(db.String(100))

    def __repr__(self):
        return '<Cliente %r>' % self.nro_dni
