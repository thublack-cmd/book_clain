'''
Cubatta Ludopatia Blueprint
    '''

from flask import Blueprint

ludopatia_cub = Blueprint('ludopatia_cub', __name__, url_prefix='/ludopatia/cubatta/')

from . import views
