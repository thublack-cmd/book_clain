from datetime import timedelta

class Config:
    SECRET_KEY = "b'_5#y2LF4Q8z\n\xec]/"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_BINDS = {
        'uchukuta': 'sqlite:///db.sqlite3'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USE_SESSION_FOR_NEXT = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=15)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_DEFAULT_SENDER = 'jgozar@losalamosgroup.com'
    MAIL_USERNAME = 'jgozar@losalamosgroup.com'
    MAIL_PASSWORD = '2@Spartans#005'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
