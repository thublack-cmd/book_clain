'''
Encuesta Blueprint
    '''

from flask import Blueprint

etribeca = Blueprint('etribeca', __name__, url_prefix='/encuesta/tribeca')

from . import views
