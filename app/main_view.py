# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from sqlalchemy import extract

# from APP
# from .models import db, Clain_cub, Clain_tri, Clain_mon, Clain_kav, Clain_sie, Clain_mag, Clain_cas, Answer_cub, Answer_tri, Answer_mon, Answer_kav, Answer_sie, Answer_mag, Answer_cas, Clain_uchu_zarate, Answer_uchu_zarate, Clain_uchu_proceres, Answer_uchu_proceres
from .models import *
from .mail import send_mail_close


def entry_point(sala):
    if sala == 'cubatta':
        clain_db = Clain_cub
        view = 'cubatta.audit_view'
        answer_db = Answer_cub
        e_sender = 'cubatta.sala@gmail.com'
        e_name = 'Sala Cubatta'
    elif sala == 'tribeca':
        clain_db = Clain_tri
        view = 'tribeca.audit_view'
        answer_db = Answer_tri
        e_sender = 'tribeca.sala@gmail.com'
        e_name = 'Sala Tribeca'
    elif sala == 'montreal':
        clain_db = Clain_mon
        view = 'montreal.audit_view'
        answer_db = Answer_mon
        e_sender = 'montreal.sala@gmail.com'
        e_name = 'Sala Montreal'
    elif sala == 'kavari':
        clain_db = Clain_kav
        view = 'kavari.audit_view'
        answer_db = Answer_kav
        e_sender = 'kavari.sala@gmail.com'
        e_name = 'Sala Kavari'
    elif sala == 'siete':
        clain_db = Clain_sie
        view = 'siete.audit_view'
        answer_db = Answer_sie
        e_sender = 'lasiete.sala@gmail.com'
        e_name = 'Sala La Siete'
    elif sala == 'magia':
        clain_db = Clain_mag
        view = 'magia.audit_view'
        answer_db = Answer_mag
        e_sender = 'magia.sala1@gmail.com'
        e_name = 'Sala Magia'
    elif sala == 'cassino':
        clain_db = Clain_cas
        view = 'cassino.audit_view'
        answer_db = Answer_cas
        e_sender = 'cassino.sala@gmail.com'
        e_name = 'Sala Cassino'
    elif sala == 'zarate':
        clain_db = Clain_uchu_zarate
        view = 'zarate.audit_view'
        answer_db = Answer_uchu_zarate
    elif sala == 'proceres':
        clain_db = Clain_uchu_proceres
        view = 'proceres.audit_view'
        answer_db = Answer_uchu_proceres
    elif sala == 'huacho':
        clain_db = Clain_uchu_huacho
        view = 'huacho.audit_view'
        answer_db = Answer_uchu_huacho
    elif sala == 'huarmey':
        clain_db = Clain_uchu_huarmey
        view = 'huarmey.audit_view'
        answer_db = Answer_uchu_huarmey
    else:
        clain_db = Clain_uchu_casma
        view = 'casma.audit_view'
        answer_db = Answer_uchu_casma

    datos = {
        'clain_db': clain_db,
        'view': view,
        'answer_db': answer_db,
        'e_sender': e_sender,
        'e_name': e_name
            }

    return datos


def audit_main(sala, request):

    datos = entry_point(sala)
    # Years available for search
    dates = datos['clain_db'].query.with_entities(extract('year', datos['clain_db'].date).distinct())

    if request.method == 'POST':
        # Clain search module
        if 'client' in request.form:
            if request.form['client'] or request.form['month'] or request.form['day'] or request.form['year']:
                c_name = request.form['client']
                date_month = request.form["month"]
                date_day = request.form["day"]
                date_year = request.form["year"]

                q_search = search_view(c_name, date_month, date_day, date_year, datos['clain_db'])

                if q_search == 0 or q_search.count() == 0:
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
                        'dates': dates,
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
                'resp': request.form['detail_dis'],
                'sala': sala,
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
            'dates': dates,
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


def search_view(name, d_month, d_day, d_year, clain):
    '''
        Search module
        '''

    dia = str(d_day)
    mes = str(d_month)
    annio = str(d_year)
    date_large = annio + '-' + mes + '-' + dia

    ## Search by serial or DNI or client name, respectly more date
    if name:
        if (clain.query.filter(clain.serial == name)).count() != 0:
            clain_query = clain.serial
            q = info_client_search(clain, clain_query, name, date_large, dia, mes, annio)
            return q

        elif (clain.query.filter(clain.nro_doc == name)).count() != 0:
            clain_query = clain.nro_doc
            q = info_client_search(clain, clain_query, name, date_large, dia, mes, annio)
            return q

        elif (clain.query.filter(clain.name.contains(name))).count() != 0:
            clain_query = clain.name
            q = info_client_search(clain, clain_query, name, date_large, dia, mes, annio)
            return q
        else:
            q = 0
            return q

    ## Search date complete
    elif d_day and d_month and d_year:
        q = clain.query.filter(clain.date.contains(date_large))
        return q

    ## Search month + year
    elif d_month and d_year:
        date_month_year = annio + '-' + mes
        q = clain.query.filter(clain.date.contains(date_month_year))
        return q

    ## Search month + day
    elif d_month and d_day:
        date_month_day = mes + '-' + dia
        q = clain.query.filter(clain.date.contains(date_month_day))
        return q

    ## Search by year
    elif d_year:
        q = clain.query.filter(extract('year', clain.date) == annio)
        return q

    else:
        q = 0
        return q


def info_client_search(clain, clain_query, name, full_date, dia, mes, anio):
    if dia and mes and anio:
        print('serial mas fecha completa')
        q = clain.query.filter(clain_query == name, clain.date.contains(full_date))
        return q
    elif mes and anio:
        print('serial mes y ano')
        date_month_year = anio + '-' + mes
        q = clain.query.filter(clain_query == name, clain.date.contains(date_month_year))
        return q
    elif mes:
        print('serial mes')
        q = clain.query.filter(clain_query == name, extract('month', clain.date) == mes)
        return q
    elif anio:
        print('serial y ano')
        q = clain.query.filter(clain_query == name, extract('year', clain.date)  == anio)
        return q
    else:
        print('serial')
        q = clain.query.filter(clain_query == name)
        return q

