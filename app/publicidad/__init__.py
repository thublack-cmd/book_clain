'''
Publicidad Update Blueprint
    '''

from flask import Blueprint

publicidad = Blueprint('publicidad', __name__, url_prefix='/publicidad/')

from . import views
