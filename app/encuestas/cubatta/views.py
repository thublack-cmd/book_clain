# from  Python
from datetime import date, datetime

# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

# from APP
from app.main_view import audit_main, discharge_main, processed_main
from app.models import db, Clain_cub
from app.mail import send_mail_open
from . import ecubatta

import gspread

now = (date.today()).strftime('%d-%m-%Y')
now2 = (datetime.utcnow()).strftime('%Y-%m-%dT%H:%M')
sala = 'cubatta'

gc = gspread.service_account()

@ecubatta.route('/', methods=['POST', 'GET'])
def client_view():
    if request.method == 'POST':
        answer = request.form
        sh = gc.open("Surveys")

        for i in range(1, 500):
            value = sh.worksheet("Cubatta").get('A' + str(i))
            if bool(value) == False:
                sh.worksheet("Cubatta").update('A' + str(i) + ':P' + str(i),
                        [[answer["question1"], answer["question2"], answer["question3"], answer["question4"], answer["question5-1"], answer["question5-2"], answer["question5-3"], answer["question5-4"], answer["question6-1"], answer["question6-2"], answer["question6-3"], answer["question6-4"], answer["question6-5"], answer["question7"], answer["question8"], answer["question9"]]])
                break

        flash(f'Registro exitoso')
        return redirect(url_for('ecubatta.client_view'))

    data = {
            'dia': now,
            'dia2': now2,
            'sala': sala,
            }

    return render_template('encuesta.html', **data)
