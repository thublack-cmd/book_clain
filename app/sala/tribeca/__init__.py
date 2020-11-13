'''
   Tribeca Blueprint
    '''

from flask import Blueprint

tribeca = Blueprint('tribeca', __name__, url_prefix='/sala/tribeca')

from . import views
