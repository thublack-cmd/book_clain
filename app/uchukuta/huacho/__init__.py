'''
   Uchukuta Huacho Blueprint
    '''

from flask import Blueprint

huacho = Blueprint('huacho', __name__, url_prefix='/uchukuta/huacho')

from . import views
