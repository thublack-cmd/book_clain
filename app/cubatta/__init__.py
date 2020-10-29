'''
   Cubatta Blueprint
    '''

from flask import Blueprint

cubatta = Blueprint('cubatta', __name__, url_prefix='/cubatta')

from . import views
