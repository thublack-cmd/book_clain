from flask import flash, redirect

from app import create_app

app = create_app()

@app.login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Debe ingresar para ver ese contenido')
    return redirect('/auth/login')
