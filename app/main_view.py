# from Python
# from datetime import date, datetime

# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

# from APP
from .models import db, Clain_cub, Clain_tri, Clain_mon, Clain_kav, Clain_sie, Clain_mag, Clain_cas, Answer_cub, Answer_tri, Answer_mon, Answer_kav, Answer_sie, Answer_mag, Answer_cas
from .mail import send_mail_close



def entry_point(sala):
    if sala == 'cubatta':
        clain_db = Clain_cub
        view = 'cubatta.audit_view'
        answer_db = Answer_cub
    elif sala == 'tribeca':
        clain_db = Clain_tri
        view = 'tribeca.audit_view'
        answer_db = Answer_tri
    elif sala == 'montreal':
        clain_db = Clain_mon
        view = 'montreal.audit_view'
        answer_db = Answer_mon
    elif sala == 'kavari':
        clain_db = Clain_kav
        view = 'kavari.audit_viewv'
        answer_db = Answer_kav
    elif sala == 'siete':
        clain_db = Clain_sie
        view = 'siete.audit_view'
        answer_db = Answer_sie
    elif sala == 'magia':
        clain_db = Clain_mag
        view = 'magia.audit_view'
        answer_db = Answer_mag
    else:
        clain_db = Clain_cas
        view = 'cassino.audit_view'
        answer_db = Answer_cas

    datos = {
        'clain_db': clain_db,
        'view': view,
        'answer_db': answer_db
            }

    return datos


def audit_main(sala, request):

    datos = entry_point(sala)

    if request.method == 'POST':
        # Clain search module
        if 'client' in request.form:
            if request.form['client'] or request.form['date']:
                c_name = request.form['client']
                date_sea = request.form["date"]

                q_search = search_view(c_name, date_sea, datos['clain_db'])

                if q_search.count() == 0:
                    q_in = None
                    q_out = None
                else:
                    page = int(request.args.get('page', 1))
                    q_in = q_search.filter(datos['clain_db'].answer_id == None)
                    if q_in.count() == 0:
                        q_in = None
                    q_out = q_search.filter(datos['clain_db'].answer_id != None).paginate(page, per_page=5)
                    if not q_out.items:
                        q_out = None

                reclamos = {
                        'pendings': q_in,
                        'answered': q_out,
                        'sala': sala,
                        }

                return render_template('audit.html', **reclamos)

            else:
                flash('Introduce un termino para realizar la busqueda')

                return redirect(url_for(datos['view']))

        new_discharge = datos['answer_db'](
                answer_con = request.form['detail_dis'],
                id_user = current_user.id
                )
        db.session.add(new_discharge)
        db.session.commit()

        # Save id discharge on clain table
        add_discharge(request.form['id_clain'], sala)

        # Get row of Clain table
        q = datos['clain_db'].query.get(request.form['id_clain'])
        data = {
                'email': q.email,
                'tipo': q.type_claim,
                'resp': request.form['detail_dis']
                }
        send_mail_close(**data)

        flash('Descargo guardado exitosamente')

        return redirect(url_for(datos['view']))


    # Method GET section
    page = int(request.args.get('page', 1))
    q_in = datos['clain_db'].query.filter(datos['clain_db'].answer_id == None)
    if q_in.count() == 0:
        q_in = None
    q_out = datos['clain_db'].query.filter(datos['clain_db'].answer_id != None)\
            .paginate(page, per_page=5)
    if not q_out.items:
        q_out = None

    reclamos = {
            'pendings': q_in,
            'answered': q_out,
            'sala': sala,
            }

    return render_template('audit.html', **reclamos)


def add_discharge(id_clain, sala):

    datos = entry_point(sala)

    # Find last answer ID
    discharge = datos['answer_db'].query.order_by(datos['answer_db'].created_at.desc()).first()

    save_id = datos['clain_db'].query.get(id_clain)
    save_id.answer_id = discharge.id
    db.session.commit()


def discharge_main(id, sala):

    datos = entry_point(sala)

    q = datos['clain_db'].query.get(id)

    if not q.answer_id:
        data = {
                'q': q,
                'sala': sala,
                }
        return render_template('discharge.html', **data)

    flash('Ese reclamo ya fue procesado')
    return redirect(url_for(datos['view']))


def processed_main(id, sala):

    datos = entry_point(sala)

    q = datos['clain_db'].query.get(id)

    if not q.answer_id:
        flash('Este reclamo no ha sido atendido')
        return redirect(url_for(datos['view']))

    data = {
            'q': q,
            'sala': sala,
            }

    return render_template('detail.html', **data)


def search_view(name, d_search, clain):
    '''
        Search module
        '''
    if name and d_search:
        q = clain.query.filter(clain.name.contains(name), clain.date.contains(d_search))
        return q
    elif name:
        q = clain.query.filter(clain.name.contains(name))
        return q
    elif d_search:
        q = clain.query.filter(clain.date.contains(d_search))
        return q
    else:
        q = 0
        return q

# db.create_all()
