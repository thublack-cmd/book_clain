# from  Python
from datetime import date, datetime

# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

# from APP
from app.main_view import audit_main, discharge_main, processed_main
from app.models import db, Clain_mon
from app.mail import send_mail_open
from . import montreal

now = (date.today()).strftime('%d-%m-%Y')
sala = 'montreal'

@montreal.route('/cliente', methods=['POST', 'GET'])
def client_view():
    if request.method == 'POST':
        d = datetime.strptime(request.form["date"], "%Y-%m-%dT%H:%M")
        new_clain = Clain_mon(
                name=request.form["name"],
                type_doc=request.form["type_doc"],
                nro_doc=request.form["document"],
                email=request.form["contact"],
                address=request.form["domicilio"],
                date=d,
                type_claim=request.form["type_obj"],
                amount=request.form["amount"],
                detail=request.form["detail"],
                )
        db.session.add(new_clain)
        db.session.commit()

        data = {
                'email': request.form['contact'],
                'tipo': request.form['type_obj'],
                }
        send_mail_open(**data)

        flash(f'Registro exitoso, en breve le responderemos al correo {request.form["contact"]}')
        return redirect(url_for('montreal.client_view'))

    data = {
            'dia': now,
            'sala': sala,
            }

    return render_template('cliente.html', **data)


@montreal.route('/', methods=['POST', 'GET'])
@login_required
def audit_view():

    a = audit_main(sala, request)

    return a


@montreal.route('/<int:id>/descargo')
@login_required
def discharge_view(id):

    d = discharge_main(id, sala)

    return d


@montreal.route('/<int:id>/detalle')
@login_required
def processed_view(id):

    p = processed_main(id, sala)

    return p
