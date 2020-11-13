'''
   Kavari Blueprint
    '''

from flask import Blueprint

kavari = Blueprint('kavari', __name__, url_prefix='/sala/kavari')

from . import views
