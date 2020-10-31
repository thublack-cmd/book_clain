'''
   Magia Blueprint
    '''

from flask import Blueprint

magia = Blueprint('magia', __name__, url_prefix='/magia')

from . import views
