from datetime import timedelta

class Config:
    SECRET_KEY = "b'_5#y2LF4Q8z\n\xec]/"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://book:accessD8-clain@172.20.20.210/book_clain'
    SQLALCHEMY_BINDS = {
        'uchukuta': 'mysql+pymysql://book:accessD8-clain@172.20.20.210/uchu_book_clain'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USE_SESSION_FOR_NEXT = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=15)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    #MAIL_DEFAULT_SENDER = 'central.salas@gmail.com'
    MAIL_USERNAME = 'cubatta.sala@gmail.com'
    MAIL_PASSWORD = 'sala.cubatta'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
