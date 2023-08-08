'''
Encuesta Blueprint
    '''

from flask import Blueprint

ekavari = Blueprint('ekavari', __name__, url_prefix='/encuesta/kavari')

from . import views
