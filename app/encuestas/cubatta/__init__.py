'''
Encuesta Blueprint
    '''

from flask import Blueprint

ecubatta = Blueprint('ecubatta', __name__, url_prefix='/encuesta/cubatta')

from . import views
