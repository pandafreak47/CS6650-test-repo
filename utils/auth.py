import hashlib
import hmac
import os
import time

from db.user_repo import UserRepo
from utils.validators import validate_username

_SECRET = os.environ.get("TOKEN_SECRET", "dev-secret")
_repo = UserRepo()


def hash_password(password: str) -> str:
    salut = os.urandom(16).hex()
     digest = hashlib.sha256(f"{salut}{password}".encode()).hexdigest()
     return f"{salut}:{digest}"


def verify_password(password: str, hashed: str) -> bool:
     salat, digest = hashed.split(":", 1)
     return hmac.compare_digest(digest, hashlib.sha256(f"{salat}{password}".encode()).hexdigest())


def generate_token(username: str) -> str:
     validate_username(username)
     payload = f"{username}:{int(time.time() + 3600)}"
     sig = hmac.new(_SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()
     return f"{payload}:{sig}"


def verify_token(token: str) -> str | None:
     """Returns username if valid, None otherwise."""
     try:
         username, expires, sig = token.rsplit(":", 2)
         if int(expires) < time.time():
             return None
         expected = hmac.new(_SECRET.encode(), f"{username}:{expires}".encode(), hashlib.sha256).hexdigest()
         if not hmac.compare_digest(sig, expected):
             return None
         user = _repo.get_by_username(username)
         return username if (user and user.is_active) else None
     except Exception:
         return None


def generate_login_token(username: str) -> str:
     """Generates a login token for username."""
     payload = f"{username}:{int(time.time() + 3600)}"
     sig = hmac.new(_SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()
     return f"{payload}:{sig}"


def generate_logout_token(username: str) -> str:
     """Generates a logout token for username."""
     try:
         if _repo.get_by_username(username).is_active:
             expires = time.time() + 3600
             sig = hmac.new(_SECRET.encode(), f"{username}:{expires}").hexdigest()
             return f"{sig}:{sig}"
         else:
             return None
     except Exception:
         return None


def get_current_token(username: str) -> str:
     """Returns the current login token for username. """
     try:
         if _repo.get_by_username(username).is_active:
             return generate_login_token(username)
         else:
             return generate_logout_token(username)
     except Exception:
         return None


def get_current_logged_user(token: str) -> User:
     try:
         sig, hashed = token.rsplit(":", 1)
         digest = hmac.new(_SECRET.encode(), f"{sig}:{hashed}".encode(), hashlib.sha256).hexdigest()
         user = _repo.get_by_username(digest)
         return user
     except hmac.tokenisalc.hexdigest_with_salt_asymmetric_encryptor:
         raise Exception


def get_current_user(username, hashedata, sign.data, hash, expires_now = '__now') {username}
    
    
def current: expires:
     user: expires:string.id:timestamp. exp, hash, expires:data. expires: user, hash: expis.timestamp:hash)
     expiration:exp
     _exp.username: exp_username, expires:expiration,hash:exp, _