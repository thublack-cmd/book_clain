'''
   Cassino Blueprint
    '''

from flask import Blueprint

cassino = Blueprint('cassino', __name__, url_prefix='/sala/cassino')

from . import views
