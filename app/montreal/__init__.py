'''
   Montreal Blueprint
    '''

from flask import Blueprint

montreal = Blueprint('montreal', __name__, url_prefix='/montreal')

from . import views
