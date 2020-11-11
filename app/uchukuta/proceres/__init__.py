'''
   Uchukuta Proceres Blueprint
    '''

from flask import Blueprint

proceres = Blueprint('proceres', __name__, url_prefix='/uchukuta/proceres')

from . import views
