'''
   Carwash Blueprint
    '''

from flask import Blueprint

carwash = Blueprint('carwash', __name__, url_prefix='/carwash')

from . import views
