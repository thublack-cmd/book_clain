# from  Python
from datetime import date, datetime

# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

# from APP
from app.main_view import audit_main, discharge_main, processed_main
from app.models import db, Clain_cas
from app.mail import send_mail_open
from . import cassino

now = (date.today()).strftime('%d-%m-%Y')
now2 = (datetime.utcnow()).strftime('%Y-%m-%dT%H:%M:%S')
sala = 'cassino'

@cassino.route('/cliente', methods=['POST', 'GET'])
def client_view():
    if request.method == 'POST':
        breakpoint();
        d = datetime.strptime(request.form["date"], "%Y-%m-%dT%H:%M")

        # if not request.form["amount"]:
        #     amount_value = 0
        # else:
        #     amount_value = request.form["amount"]

        # add serial to table
        last_clain = Clain_cas.query.order_by(Clain_cas.created_at.desc()).first()
        if not last_clain:
            serial = 'SCA-1'
        else:
            serial = 'SCA-' + str(last_clain.id)

        new_clain = Clain_cas(
                serial=serial,
                name=request.form["name"],
                type_doc=request.form["type_doc"],
                nro_doc=request.form["document"],
                email=request.form["contact"],
                #address=request.form["domicilio"],
                date=d,
                type_claim=request.form["type_obj"],
                # amount=amount_value,
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
        return redirect(url_for('cassino.client_view'))

    data = {
            'dia': now,
            'dia2': now2,
            'sala': sala,
            }

    return render_template('cliente.html', **data)


@cassino.route('/', methods=['POST', 'GET'])
@login_required
def audit_view():

    a = audit_main(sala, request)

    return a


@cassino.route('/<int:id>/descargo')
@login_required
def discharge_view(id):

    d = discharge_main(id, sala)

    return d


@cassino.route('/<int:id>/detalle')
@login_required
def processed_view(id):

    p = processed_main(id, sala)

    return p

