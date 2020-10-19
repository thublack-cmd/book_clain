# from Flask
from flask import render_template, Flask, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app.config import app, login_manager
from app.models import db, Clain, Answer
from app.mail import send_mail_open, send_mail_close

# from Python
from datetime import date, datetime

now = (date.today()).strftime('%d-%m-%Y')


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Debe ingresar para ver ese contenido')
    return redirect('/login')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        pass
    return render_template('signup.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('audit_view'))

    if request.method == 'POST':
        pass

    return render_template('login.html')


@app.route('/', methods=['POST', 'GET'])
def client_view():
    if request.method == 'POST':
        d = datetime.strptime(request.form["date"], "%Y-%m-%dT%H:%M")
        new_clain = Clain(
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


@app.route('/gestion', methods=['GET', 'POST'])
@login_required
def audit_view():
    if request.method == 'POST':
        new_discharge = Answer(
                answer_con=request.form['detail_dis']
                )
        db.session.add(new_discharge)
        db.session.commit()

    # Save id discharge on clain table
        add_discharge(request.form['id_clain'])

    # Get row of Clain table
        q = Clain.query.get(request.form['id_clain'])
        data = {
                'email': q.email,
                'tipo': q.type_claim,
                'resp': request.form['detail_dis']
                }
        send_mail_close(**data)

        flash('Descargo guardado exitosamente')

        return redirect(url_for('audit_view'))

    q = Clain.query.all()
    return render_template('audit.html', reclamos=q)

def add_discharge(id_clain):
    # Find last answer ID
    discharge = Answer.query.order_by(Answer.created_at.desc()).first()

    save_id = Clain.query.get(id_clain)
    save_id.answer_id = discharge.id
    db.session.commit()


@app.route('/<int:id>/descargo')
@login_required
def discharge_view(id):

    q = Clain.query.get(id)

    if not q.answer_id:
        data = {
                'q': q,
                }
        return render_template('discharge.html', **data)

    flash('Ese reclamo ya fue procesado')
    return redirect(url_for('audit_view'))


@app.route('/<int:id>/detalle')
@login_required
def processed_view(id):
    q = Clain.query.get(id)

    if not q.answer_id:
        flash('Este reclamo no ha sido atendido')
        return redirect(url_for('audit_view'))

    return render_template('detail.html', q=q)

# db.create_all()
