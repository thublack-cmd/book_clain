'''
Encuesta Blueprint
    '''

from flask import Blueprint

encuesta = Blueprint('ecubatta', __name__, url_prefix='/encuesta/cubatta')

from . import views
