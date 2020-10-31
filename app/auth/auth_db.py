# from flask
from flask_login import UserMixin

# from APP
from app.models import User


def get_user(user_id):
    return User.query.get(user_id)

class user_data:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class user_model(UserMixin):
    def __init__(self, data_user):
        self.id = data_user.username
        self.password = data_user.password

    @staticmethod
    def query(user_id):
        user = get_user(user_id)
        data_user = user_data(
                username = user.username,
                password = user.password,
                )
        return user_model(data_user)
