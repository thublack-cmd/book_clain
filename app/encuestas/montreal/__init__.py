'''
Encuesta Blueprint
    '''

from flask import Blueprint

emontreal = Blueprint('emontreal', __name__, url_prefix='/encuesta/montreal')

from . import views
