from threading import Thread
from flask_mail import Mail, Message
from flask import current_app as book

# from . import mail

mail = Mail()

def _send_async_email(flask_app, msg):
    with flask_app.app_context():
        mail.send(msg)

def send_mail_open(tipo, email, e_name, e_sender):
    '''
        Send email to client and managers in opened process
    '''

    # send email client
    #msg = Message(f'Registro de {tipo}', recipients=[email])
    #msg.body = (f'Hemos recibido su {tipo}, en la brevedad posible estaremos respondiendole')

    #thr = Thread(target=_send_async_email, args=[book._get_current_object(), msg])
    #thr.start()

    # send email managers
    msg = Message(f'Nuevo/a {tipo}', sender=(e_name, e_sender), recipients=['central.salas@gmail.com', 'alamosmensajes@gmail.com', 'losalamosgaming@hotmail.com'])
    msg.body = ('Se ha registrado una nueva entrada en el libro de reclamaciones')

    thr = Thread(target=_send_async_email, args=[book._get_current_object(), msg])
    thr.start()
    return thr


def send_mail_close(tipo, email, resp, e_send, e_name):
    '''
        Send email to client and managers in close process
    '''

    # send email client
    #msg = Message(f'Respuesta de su {tipo}', recipients=[email])
    #msg.body = (f'Hemos atendido su {tipo} de la siguiente manera: \n {resp}')

    #thr = Thread(target=_send_async_email, args=[book._get_current_object(), msg])
    #thr.start()

    # send email managers
    msg = Message(f'Respuesta de {tipo}', sender=(e_name, e_send), recipients=['central.salas@gmail.com', 'alamosmensajes@gmail.com', 'losalamosgaming@hotmail.com'])
    msg.body = ('Se ha respondido a esta entrada')

    thr = Thread(target=_send_async_email, args=[book._get_current_object(), msg])
    thr.start()
    return thr
