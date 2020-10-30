# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required

# from  Python
from datetime import date, datetime

# from APP
from app.main_view import audit_main, discharge_main, processed_main
from app.models import db, Clain_cub
from app.mail import send_mail_open
from . import cubatta

now = (date.today()).strftime('%d-%m-%Y')
sala = 'tribeca'

@cubatta.route('/cubatta/cliente', methods=['POST', 'GET'])
def client_view():
    if request.method == 'POST':
        d = datetime.strptime(request.form["date"], "%Y-%m-%dT%H:%M")
        new_clain = Clain_cub(
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
        return redirect(url_for('client_view'))

    return render_template('cliente.html', dia=now)


@cubatta.route('/', methods=['POST', 'GET'])
@login_required
def audit_view():

    audit_main(sala, request)


@cubatta.route('/<int:id>/descargo')
@login_required
def discharge_view(id):

    discharge_main(id, sala)


@cubatta.route('/<int:id>/detalle')
@login_required
def processed_view(id):

    processed_main(id, sala)


    # if request.method == 'POST':
    #     # Clain search module
    #     if 'client' in request.form:
    #         if request.form['client'] or request.form['date']:
    #             c_name = request.form['client']
    #             date_sea = request.form["date"]

    #             q_search = search_view(c_name, date_sea)

    #             if q_search.count() == 0:
    #                 q_in = None
    #                 q_out = None
    #             else:
    #                 page = int(request.args.get('page', 1))
    #                 q_in = q_search.filter(Clain.answer_id == None)
    #                 if q_in.count() == 0:
    #                     q_in = None
    #                 q_out = q_search.filter(Clain.answer_id != None).paginate(page, per_page=5)
    #                 if not q_out.items:
    #                     q_out = None

    #             reclamos = {
    #                     'pendings': q_in,
    #                     'answered': q_out,
    #                     }

    #             return render_template('audit.html', **reclamos)

    #         else:
    #             flash('Introduce un termino para realizar la busqueda')

    #             return redirect(url_for('audit_view'))

    #     new_discharge = Answer(
    #             answer_con = request.form['detail_dis'],
    #             id_user = current_user.id
    #             )
    #     db.session.add(new_discharge)
    #     db.session.commit()

    #     # Save id discharge on clain table
    #     add_discharge(request.form['id_clain'])

    #     # Get row of Clain table
    #     q = Clain.query.get(request.form['id_clain'])
    #     data = {
    #             'email': q.email,
    #             'tipo': q.type_claim,
    #             'resp': request.form['detail_dis']
    #             }
        # send_mail_close(**data)

        # flash('Descargo guardado exitosamente')

        # return redirect(url_for('audit_view'))


    # # Method GET section
    # page = int(request.args.get('page', 1))
    # q_in = Clain.query.filter(Clain.answer_id == None)
    # if q_in.count() == 0:
        # q_in = None
    # q_out = Clain.query.filter(Clain.answer_id != None)\
        #     .paginate(page, per_page=5)

    # reclamos = {
        #     'pendings': q_in,
        #     'answered': q_out,
        #     }

    # return render_template('audit.html', **reclamos)

# def add_discharge(id_clain):
    # # Find last answer ID
    # discharge = Answer.query.order_by(Answer.created_at.desc()).first()

    # save_id = Clain.query.get(id_clain)
    # save_id.answer_id = discharge.id
    # db.session.commit()


# @app.route('/<int:id>/descargo')
# @login_required
# def discharge_view(id):

    # q = Clain.query.get(id)

    # if not q.answer_id:
        # data = {
        #         'q': q,
        #         }
        # return render_template('discharge.html', **data)

    # flash('Ese reclamo ya fue procesado')
    # return redirect(url_for('audit_view'))


# @app.route('/<int:id>/detalle')
# @login_required
# def processed_view(id):
    # q = Clain.query.get(id)

    # if not q.answer_id:
    #     flash('Este reclamo no ha sido atendido')
    #     return redirect(url_for('audit_view'))

    # return render_template('detail.html', q=q)


# def search_view(name, d_search):

    # if name and d_search:
    #     q = Clain.query.filter(Clain.name.contains(name), Clain.date.contains(d_search))
    #     return q
    # elif name:
    #     q = Clain.query.filter(Clain.name.contains(name))
    #     return q
    # elif d_search:
    #     q = Clain.query.filter(Clain.date.contains(d_search))
    #     return q
    # else:
    #     q = 0
    #     return q

