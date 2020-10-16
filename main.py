# from Flask
from flask import render_template, Flask, request, redirect, url_for, flash

from app.config import app
from app.models import db, Clain, Answer

# from Python
from datetime import date, datetime

now = (date.today()).strftime('%d-%m-%Y')

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

        return f'Registro exitoso, le responderemos a su correo {request.form["contact"]} en breve'

    return render_template('cliente.html', dia=now)


@app.route('/gestion', methods=['GET', 'POST'])
def audit_view():
    if request.method == 'POST':
        new_discharge = Answer(
                answer_con=request.form['detail_dis']
                )
        db.session.add(new_discharge)
        db.session.commit()

        add_discharge(request.form['id_clain'])

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
def discharge_view(id):

    q = Clain.query.get(id)

    if not q.answer_id:
        data = {
                'q': q,
                'id': id,
                }
        return render_template('discharge.html', **data)

    flash('Ese reclamo ya fue procesado')
    return redirect(url_for('audit_view'))

@app.route('/<int:id>/detalle')
def processed_view(id):
    q = Clain.query.get(id)

    if not q.answer_id:
        flash('Este reclamo no ha sido atendido')
        return redirect(url_for('audit_view'))

    return render_template('detail.html', q=q)

# db.create_all()
