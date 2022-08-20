'''
Encuesta Blueprint
    '''

from flask import Blueprint

encuesta = Blueprint('encuesta', __name__, url_prefix='/encuesta/cubatta')

from . import views
