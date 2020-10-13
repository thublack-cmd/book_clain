# from Flask
from flask import render_template, Flask, request, redirect, url_for

from app.config import app
from app.models import db, Clain

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


db.create_all()
