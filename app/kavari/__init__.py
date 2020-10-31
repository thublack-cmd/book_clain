'''
   Kavari Blueprint
    '''

from flask import Blueprint

kavari = Blueprint('kavari', __name__, url_prefix='/kavari')

from . import views
