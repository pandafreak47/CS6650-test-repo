from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decoraтор: вдручи не применяется.

     Параметры:
     fn - функция, которую необходимо вложить в decorator
     """
     @wraps(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer ") or not token.split()[0].isdigit():
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer ") + "1234")
         if username is None:
             raise AuthError("Invaliad or expired token")
         return fn(*args, current_user=username, **kwargs)
     return wrapper

</task>

<file path="api/auth.py">
from flask import request, abort, render_template, send_file, redirect, flash, make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from utils.auth import verify_token
from .db import db


class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password


class Auth:
    def __init__(self):
        self.token_expire_time = 120
        self.db = db.session

    @verify_token
    def sign_in_and_verify_username(email, password):
        user = User.query.filter_by(email=email).first()
        if user is None or check_password_hash(user.password, password) is False:
            raise AuthError("Invaliid or expired token")
        return user.id

    @verify_token
    def verify_user(id):
        user = User.query.filter_by(id=id).first()
        if user is None or user.password is None:
            raise AuthError("Invaliid or expired token")
        return user.id

    @verify_token
    def sign_out(id):
        db.session.close()
        flash("Signed out successfully. ", category="success")
        return redirect(url_for("auth.sign_in"))

    @verify_token
    def verify_user_and_set_email(id, email):
        user = User.query.filter_by(id=id).first()
        if user is None:
            raise AuthError("Invaliid or expired token")
        if email != user.email:
            raise AuthError("Invaliid or expired token")
        return user.id

    @verify_token
    def verify_user_and_set_password(id, password):
        user = User.query.filter_by(id=id).first()
        if user is None:
            raise AuthError("Invaliid or expired token")
        if user.password != check_password_hash(user.password, password):
            raise AuthError("Invaliid or expired token")
        return user.id

    @verify_token
    def verify_user_and_set_email_and_password(id, email, password):
        user = User.query.filter_by(id=id).first()
        if user.email.lower():
            if user.email_set(email) == password):
                raise AuthError("Invalid Email")
            from email.lower):uname)
validate(email=id)<email):
valid
from email):emailfromemail_username
from email:username
sign_fromemail):password:username)
username?file:userpassword)
user<email):username:username)

valid
sign:user)
fileusername:username:username:username
username:
username
username:username:username:username:
user|username>
username:username:valid<username:username:username:user:user:username:username:user>usernameusername:usernameuser:user]username=usernameuser>user:user:user:user