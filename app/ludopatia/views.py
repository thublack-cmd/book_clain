# from Flask
from flask import render_template, request, redirect, url_for, flash

# from APP
from app.models import db, Ludopatia_db, no_access
from . import ludopatia

import pandas

@ludopatia.route('/', methods=['POST', 'GET'])
def client_view():

    sql_db_ludo = Ludopatia_db.query.with_entities(Ludopatia_db.nro_dni).all()
    sql_db = no_access.query.with_entities(no_access.nro_dni).all()
    sql_list_ludo = []
    sql_list = []
    notInDB = 0

    for i in range(len(sql_db_ludo)):
        sql_list_ludo.append(sql_db_ludo[i][0])
    for i in range(len(sql_db)):
        sql_list.append(sql_db[i][0])

    if request.method == 'POST':
        if request.files["fileUp"]:
            with pandas.ExcelFile(request.files["fileUp"]) as xls:
                sh = pandas.read_excel(xls, header=None, dtype=str)
                if len(sh) != len(sql_db_ludo):
                    for i in range(len(sh)):
                        if sh.loc[i][1] not in sql_list_ludo:
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

        elif request.files["fileUpClient"]:
            with pandas.ExcelFile(request.files["fileUpClient"]) as xls:
                sh = pandas.read_excel(xls, header=None, dtype=str)
                if len(sh) != len(sql_db):
                    for i in range(len(sh)):
                        # breakpoint()
                        if sh.loc[i][1] not in sql_list:
                            notInDB+= 1
                            new_entry = no_access(
                                nro_dni= sh.loc[i][1],
                                name= sh.loc[i][2],
                            )
                            db.session.add(new_entry)
                            db.session.commit()
                    flash(f'Se han agregado {notInDB} personas a la base de datos')
                    return redirect(url_for('ludopatia.client_view'))
                else:
                    flash("No hay nuevas personas para agregar")

    return render_template('update.html')

@ludopatia.route('/clientes', methods=['POST', 'GET'])
def sala_view():

    if request.method == 'POST':
        sql_db = no_access.query.with_entities(no_access.nro_dni).all()
        sql_list = []
        in_list = {}
        in_DB = 0

        for i in range(len(sql_db)):
            sql_list.append(sql_db[i][0])

        with pandas.ExcelFile(request.files["fileUpdate"]) as xls:
            sh = pandas.read_excel(xls, header=None, dtype=str)
            for i in range(len(sh)):
                if sh.loc[i][0] in sql_list:
                    in_list[sh.loc[i][0]] = sh.loc[i][1]
                    in_DB+= 1
            flash(f'Se han encontrado {in_DB} personas inscritas')

            data = {
                    'user_list': in_list,
                    }

            return render_template('update_sala.html', **data)

    return render_template('update_sala.html')
