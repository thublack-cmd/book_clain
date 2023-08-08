'''
   Carwash Blueprint
    '''

from flask import Blueprint

carwash = Blueprint('carwash', __name__, url_prefix='/sala/carwash')

from . import views
