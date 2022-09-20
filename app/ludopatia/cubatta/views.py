# from  Python
from datetime import date, datetime

# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

# from APP
from app.main_view import audit_main, discharge_main, processed_main
from app.models import db, Ludopatia_db, ingreso_cubatta
from app.mail import send_mail_open
from . import ludopatia_cub

import pandas, pygame

sala = 'cubatta'

# Inicializacion de librerias para el sonido
pygame.init()
pygame.mixer.init()
dont_access = pygame.mixer.Sound("./app/static/alerta1.wav")
access = pygame.mixer.Sound("./app/static/BIENVENIDA.wav")


@ludopatia_cub.route('/', methods=['POST', 'GET'])
def client_view():

    sql_db = Ludopatia_db.query.with_entities(Ludopatia_db.nro_dni).all()
    sql_list = []

    for i in range(len(sql_db)):
        sql_list.append(sql_db[i][0])

    if request.method == 'POST':
        answer = request.form

        if answer["input-num"] in sql_list:
            flash("PROHIBIDO EL INGRESO", 'error')
            pygame.mixer.Sound.play(dont_access)
            new_log = ingreso_cubatta(
                nro_document = answer["input-num"]
            )
            db.session.add(new_log)
            db.session.commit()
            return redirect(url_for('ludopatia_cub.client_view'))
        else:
            flash("BIENVENIDO A LA SALA")
            pygame.mixer.Sound.play(access)
            new_log = ingreso_cubatta(
                nro_document = answer["input-num"]
            )
            db.session.add(new_log)
            db.session.commit()
            return redirect(url_for('ludopatia_cub.client_view'))

    data = {
            'sala': sala,
            }

    with pandas.ExcelFile("~/Downloads/DBLudopatia.xlsx") as xls:
        sh = pandas.read_excel(xls, "LUDO_DB")
        if len(sh["Nro. Documento"]) != len(sql_db):
            for index, row in sh.iterrows():
                if row['Nro. Documento'] not in sql_list:
                    new_entry = Ludopatia_db(
                        num_reg= row['Num. Reg.'],
                        nro_dni= row['Nro. Documento'],
                        name_dni= row['Nombres y Apellidos']
                    )
                    db.session.add(new_entry)
                    db.session.commit()
                else:
                    print(str(row['Num. Reg.']) + " SI ESTA \n")

    return render_template('ludopatia.html', **data)
