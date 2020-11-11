'''
   Uchukuta Zarate Blueprint
    '''

from flask import Blueprint

zarate = Blueprint('zarate', __name__, url_prefix='/uchukuta/zarate')

from . import views
