from flask import Flask, render_template

from datetime import date

now = (date.today()).strftime('%d-%m-%Y')

app = Flask(__name__)

@app.route('/')
def client_view():
    return render_template('cliente.html', dia=now)
