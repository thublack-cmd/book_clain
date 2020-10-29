from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import db, get_user, user_data, user_model, User
from . import auth


@auth.route('/signup', methods=['POST', 'GET'])
@login_required
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if request.form['sudo'] == 'on':
            sudo = True
        else:
            sudo = False

        user_ver = get_user(username)

        if not user_ver:
            password_hash = generate_password_hash(password)

            save_user = User(
                    username = username,
                    password = password_hash,
                    is_superuser= sudo,
                    first_name = request.form['first_name'],
                    last_name = request.form['last_name'],
                    )
            db.session.add(save_user)
            db.session.commit()

            flash('Registro exitoso')

            return redirect('auth.signup')

    return render_template('signup.html')


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('audit_view'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user_ver = get_user(username)

        if user_ver:
            if check_password_hash(user_ver.password, password):

                userdata = user_data(username, password)
                user = user_model(userdata)

                login_user(user)
                flash('Bienvenido')
                return redirect(url_for('audit_view'))
            else: flash('Contrasena incorrecta')
        else: flash('Usuario no existe')

    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Se ha cerrado la sesion exitosamente')

    return redirect(url_for('auth.login'))
