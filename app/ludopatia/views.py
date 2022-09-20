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

    for i in range(len(sql_db)):
        sql_list.append(sql_db[i][0])

    if request.method == 'POST':

            return redirect(url_for('ludopatia_cub.client_view'))

    data = {
            'sala': sala,
            }

    with pandas.ExcelFile("~/Downloads/DBLudopatia.xlsx") as xls:
        sh = pandas.read_excel(xls, "LUDO_DB")
        if len(sh["Nro. Documento"]) != len(sql_db):
            for index, row in sh.iterrows():
                if row['Nro. Documento'] not in sql_list:
                    new_entry = Ludopatia_db(
                        num_reg= row['Num. Reg.'],
                        nro_dni= row['Nro. Documento'],
                        name_dni= row['Nombres y Apellidos']
                    )
                    db.session.add(new_entry)
                    db.session.commit()
                else:
                    print(str(row['Num. Reg.']) + " SI ESTA \n")

    return render_template('ludopatia.html', **data)
