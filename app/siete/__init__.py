'''
   La Siete Blueprint
    '''

from flask import Blueprint

siete = Blueprint('siete', __name__, url_prefix='/siete')

from . import views
