'''
   Magia Blueprint
    '''

from flask import Blueprint

magia = Blueprint('magia', __name__, url_prefix='/sala/magia')

from . import views
