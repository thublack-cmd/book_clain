# from Flask
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

# from APP
from app import create_app
# from app.config import login_manager
from app.models import db, Clain, Answer, get_user, user_data, user_model, User
from app.mail import send_mail_open, send_mail_close

# from Python
from datetime import date, datetime

app = create_app()
now = (date.today()).strftime('%d-%m-%Y')

@app.login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Debe ingresar para ver ese contenido')
    return redirect('/login')

@app.route('/signup', methods=['POST', 'GET'])
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

            return redirect('/signup')

    return render_template('signup.html')


@app.route('/login', methods=['POST', 'GET'])
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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Se ha cerrado la sesion exitosamente')

    return redirect(url_for('login'))


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
        # Clain search module
        if 'client' in request.form:
            if request.form['client'] or request.form['date']:
                c_name = request.form['client']
                date_sea = request.form["date"]

                q_search = search_view(c_name, date_sea)

                if q_search.count() == 0:
                    q_in = None
                    q_out = None
                else:
                    page = int(request.args.get('page', 1))
                    q_in = q_search.filter(Clain.answer_id == None)
                    if q_in.count() == 0:
                        q_in = None
                    q_out = q_search.filter(Clain.answer_id != None).paginate(page, per_page=5)
                    if not q_out.items:
                        q_out = None

                reclamos = {
                        'pendings': q_in,
                        'answered': q_out,
                        }

                return render_template('audit.html', **reclamos)

            else:
                flash('Introduce un termino para realizar la busqueda')

                return redirect(url_for('audit_view'))

        new_discharge = Answer(
                answer_con = request.form['detail_dis'],
                id_user = current_user.id
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


    # Method GET section
    page = int(request.args.get('page', 1))
    q_in = Clain.query.filter(Clain.answer_id == None)
    if q_in.count() == 0:
        q_in = None
    q_out = Clain.query.filter(Clain.answer_id != None)\
            .paginate(page, per_page=5)

    reclamos = {
            'pendings': q_in,
            'answered': q_out,
            }

    return render_template('audit.html', **reclamos)

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


def search_view(name, d_search):

    if name and d_search:
        q = Clain.query.filter(Clain.name.contains(name), Clain.date.contains(d_search))
        return q
    elif name:
        q = Clain.query.filter(Clain.name.contains(name))
        return q
    elif d_search:
        q = Clain.query.filter(Clain.date.contains(d_search))
        return q
    else:
        q = 0
        return q

# db.create_all()
