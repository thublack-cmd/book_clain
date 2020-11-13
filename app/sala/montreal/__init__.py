'''
   Montreal Blueprint
    '''

from flask import Blueprint

montreal = Blueprint('montreal', __name__, url_prefix='/sala/montreal')

from . import views
