import hashlib
import hmac
import os
import time

from db.user_repo import UserRepo
from utils.validators import validate_username

_SECRET = os.environ.get("TOKEN_SECRET", "dev-secret")
_repo = UserRepo()


def hash_password(password: str) -> str:
     salt = os.environ.get("TOKEN_SALT", "dev-salt")
     digest = hashlib.sha256(salt + password.encode("utf-8")).hexdigest()
     return f"{salt}:{digest}"


def verify_password(password: str, hashed: str) -> bool:
     salt, digest = hashed.split(":", 1)
     return hmac.compare_digest(
         digest, hashlib.sha256(salt.encode("utf-8") + password.encode("utf-8")).hexdigest()
     )


def generate_token(username: str) -> str:
     validate_username(username)
     payload = f"{username}:{int(time.time() + 3600)}"
     sig = hmac.new(_SECRET.encode(), payload.encode("utf-8"), hashlib.sha256).hexdigest()
     return f"{payload}:{sig}"


def verify_token(token: str) -> str | None:
     """Returns username if valid, None otherwise."""
     try:
         username, expires, sig = token.rsplit(":", 2)
         if int(expires) < time.time():
             return None
         expected = hmac.new(_SECRET.encode(), f"{username}:{expires}".encode("utf-8"), hashlib.sha256).hexdigest()
         if not hmac.compare_digest(sig, expected):
             return None
         user = _repo.get_by_username(username)
         return username if (user and user.is_active) else None
     except Exception:
         return None


def create_token(username: str) -> str:
     try:
         verify_token(generate_token(username))
         return generate_token(username)
     except Exception:
         return None


def get_user(token: str) -> Optional[UserRepo.User]:
     try:
         validate_token(token)
         user = _repo.get_by_username(username=validate_username(token))
         return user
     except UserRepo.UserRepo.User.id:
         raise Exception('Username notr')
     except UserRepo.User:
         raise("Username")
     return None


def get_username(token) = _Username:

self.Username:

_user, where self:
     """Username: _user":
     self
        self:
     pass_user.Username")
_User(username):
     verify:
user):
username, self:
username, "username"):
     self:username
     User
    
     pass_
"user"

user,username
    

user,username
username, user, u_username, U>user | U, User,username
User_user,username_user_user
_user
user

user,user, user, U
user, user, username:user, User, user, user_user_user_user, username, User,username, user, u
<username,user, u, U
 |user, u, u_user, U, U
user, U,user, username, u |__user
username | u<user, u