# from  Python
from datetime import date, datetime

# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

# from APP
from app.main_view import audit_main, discharge_main, processed_main
from app.models import db, Clain_cub
from app.mail import send_mail_open
from . import ludopatia

import gspread, pygame

now = (date.today()).strftime('%d-%m-%Y')
now2 = (datetime.utcnow()).strftime('%Y-%m-%dT%H:%M')
sala = 'cubatta'

# Inicializacion de librerias para el sonido
pygame.init()
pygame.mixer.init()
dont_access = pygame.mixer.Sound("./app/static/alerta1.wav")
access = pygame.mixer.Sound("./app/static/BIENVENIDA.wav")

gc = gspread.service_account()

@ludopatia.route('/', methods=['POST', 'GET'])
def client_view():
    if request.method == 'POST':
        answer = request.form
        sh = gc.open("Ludopatia-DB")

        cell = sh.worksheet("MINCETUR_DB").find("41338207")
        if bool(cell):
            flash("PROHIBIDO EL INGRESO", 'error')
            pygame.mixer.Sound.play(dont_access)
            return redirect(url_for('ludopatia.client_view'))
        else:
            flash("BIENVENIDO A LA SALA")
            pygame.mixer.Sound.play(access)
            return redirect(url_for('ludopatia.client_view'))

    data = {
            'sala': sala,
            }

    return render_template('ludopatia.html', **data)
