'''
   Uchukuta Huarmey Blueprint
    '''

from flask import Blueprint

huarmey = Blueprint('huarmey', __name__, url_prefix='/uchukuta/huarmey')

from . import views
