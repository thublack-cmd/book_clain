'''
   Cassino Blueprint
    '''

from flask import Blueprint

cassino = Blueprint('cassino', __name__, url_prefix='/cassino')

from . import views
