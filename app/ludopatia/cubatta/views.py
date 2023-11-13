# from  Python
from datetime import date, datetime

# from Flask
from flask import render_template, request, redirect, url_for, flash

# from APP
from . import ludopatia_cub

sala = 'cubatta'

@ludopatia_cub.route('/', methods=['POST', 'GET'])
def client_view():

    if request.method == 'POST':
        answer = request.form
        day = str(datetime.now())

        with open('./app/ludopatia/cubatta/clientes', 'a') as p:
            p.write(day + " " + answer["input-num"] + '\n')

        with open('./app/ludopatia/cubatta/dbludopatia', 'r') as f:
            a = f.read()

            if answer["input-num"] in a:
                flash("PROHIBIDO EL INGRESO", 'error')
                return redirect(url_for('ludopatia_cub.client_view'))
            else:
                flash("BIENVENIDO A LA SALA")
            return redirect(url_for('ludopatia_cub.client_view'))

    data = {
            'sala': sala,
            }

    return render_template('ludopatia.html', **data)
