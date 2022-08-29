'''
Ludopatia Blueprint
    '''

from flask import Blueprint

ludopatia = Blueprint('ludopatia', __name__, url_prefix='/ludopatia/')

from . import views
