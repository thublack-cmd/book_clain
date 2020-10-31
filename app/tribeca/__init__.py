'''
   Tribeca Blueprint
    '''

from flask import Blueprint

tribeca = Blueprint('tribeca', __name__, url_prefix='/tribeca')

from . import views
