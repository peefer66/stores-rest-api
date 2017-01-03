from werkzeug.security import safe_str_cmp
from models.user_model import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)

    # if user and user.password == password:  # If user exists and the passwords match
    if user and safe_str_cmp(user.password, password):  # =>safer way for comparison in case using 2.7 or other encoding
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
