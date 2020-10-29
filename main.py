# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

# from APP
from app import create_app
from app.models import db, Clain, Answer
from app.mail import send_mail_open, send_mail_close

# from Python
from datetime import date, datetime

app = create_app()
now = (date.today()).strftime('%d-%m-%Y')

@app.login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Debe ingresar para ver ese contenido')
    return redirect('/auth/login')


def entry_point(sala):
    clain_db = Clain + '_' + sala
    view = 'audit_viewt' + '_' + sala
    answer_db = Answer + '_' + sala

    datos = {
        'clain_db': clain_db,
        'view': view,
        'answer_db': answer_db
            }

    return datos


def audit_view(sala, request):

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
        add_discharge(request.form['id_clain'])

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

    reclamos = {
            'pendings': q_in,
            'answered': q_out,
            }

    return render_template('audit.html', **reclamos)

def add_discharge(id_clain):
    # Find last answer ID
    discharge = Answer.query.order_by(Answer.created_at.desc()).first()

    save_id = Clain.query.get(id_clain)
    save_id.answer_id = discharge.id
    db.session.commit()


def discharge_view(id):

    q = Clain.query.get(id)

    if not q.answer_id:
        data = {
                'q': q,
                }
        return render_template('discharge.html', **data)

    flash('Ese reclamo ya fue procesado')
    return redirect(url_for('audit_view'))


def processed_view(id):
    q = Clain.query.get(id)

    if not q.answer_id:
        flash('Este reclamo no ha sido atendido')
        return redirect(url_for('audit_view'))

    return render_template('detail.html', q=q)


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
