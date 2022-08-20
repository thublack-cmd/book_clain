# from  Python
from datetime import date, datetime

# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

# from APP
from app.main_view import audit_main, discharge_main, processed_main
from app.models import db, Clain_cub
from app.mail import send_mail_open
from . import encuesta

now = (date.today()).strftime('%d-%m-%Y')
now2 = (datetime.utcnow()).strftime('%Y-%m-%dT%H:%M')
sala = 'encuesta'

@encuesta.route('/', methods=['POST', 'GET'])
def client_view():

    data = {
            'dia': now,
            'dia2': now2,
            'sala': sala,
            }

    return render_template('encuesta.html', **data)
