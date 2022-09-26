# from Flask
from flask import render_template, request, redirect, url_for, flash

# from APP
from app.models import db, Ludopatia_db
from . import ludopatia

import pandas

sala = 'cubatta'

@ludopatia.route('/', methods=['POST', 'GET'])
def client_view():

    sql_db = Ludopatia_db.query.with_entities(Ludopatia_db.nro_dni).all()
    sql_list = []
    notInDB = 0

    for i in range(len(sql_db)):
        sql_list.append(sql_db[i][0])

    if request.method == 'POST':
        with pandas.ExcelFile(request.files["fileUp"]) as xls:
            sh = pandas.read_excel(xls, header=None)
            breakpoint()
            if len(sh) != len(sql_db):
                for i in range(len(sh)):
                    # breakpoint()
                    if sh.loc[i][1] not in sql_list:
                        notInDB+= 1
                        new_entry = Ludopatia_db(
                            num_reg= sh.loc[i][0],
                            nro_dni= sh.loc[i][1],
                            name_dni= sh.loc[i][2],
                        )
                        db.session.add(new_entry)
                        db.session.commit()
                flash(f'Se han agregado {notInDB} personas a la base de datos')
                return redirect(url_for('ludopatia.client_view'))
            else:
                flash("No hay nuevas personas para agregar")

    data = {
            'sala': sala,
            }

    return render_template('update.html', **data)
