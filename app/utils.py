import uuid
import random
from functools import wraps
from flask import redirect, url_for
from flask_login import current_user
from app.extensions import login_manager
from app.modules.user.models import UserTokenModel


@login_manager.user_loader
def user_loader(token):
    token_obj = UserTokenModel.query.filter_by(token=token).first() or None
    if token_obj:
        return token_obj.user
    return None

# Decorator function for when user tries to access routes that are strictly for non-authenticated users
# such as login and register routes. 
def must_not_be_authed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for("dashboard.dashboard"))
        return func(*args, **kwargs)
    return wrapper



def generate_random_string(min_length, max_length):
    # generate a random number between min_length and max_length (inclusive)
    rand_length = random.randint(min_length, max_length)

    current_string = ""

    # while loop will connect random string together until its length is bigger than or equals to rand_length
    while(len(current_string) < rand_length):
        current_string += str(uuid.uuid4().hex)
    
    # make sure that return string is the size of the rand_length
    return current_string[:rand_length]

