from flask import flash, redirect, url_for

from app import create_app

app = create_app()

# @app.login_manager.unauthorized_handler
# def unauthorized_callback():
#     flash('Debe ingresar para ver ese contenido')
#     return redirect('/auth/login')

@app.route('/')
def index():
    return redirect(url_for('cubatta.audit_view'))

if __name__ == '__main__':
    app.run()
