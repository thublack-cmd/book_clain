'''
   Uchukuta Casma Blueprint
    '''

from flask import Blueprint

casma = Blueprint('casma', __name__, url_prefix='/uchukuta/casma')

from . import views
