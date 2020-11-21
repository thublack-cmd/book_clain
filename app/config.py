from datetime import timedelta

class Config:
    SECRET_KEY = "b'_5#y2LF4Q8z\n\xec]/"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://book:pruebaDB@localhost/book_clain'
    SQLALCHEMY_BINDS = {
        'uchukuta': 'mysql+pymysql://book:pruebaDB@localhost/uchu_book_clain'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USE_SESSION_FOR_NEXT = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_DEFAULT_SENDER = 'central.salas@gmail.com'
    MAIL_USERNAME = 'central.salas@gmail.com'
    MAIL_PASSWORD = 'password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
