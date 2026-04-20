<file path="utils/auth.py">
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
     digest = hashlib.sha256(f"{salt}{password}").hexdigest()
     return f"{salt}:{digest}"


def verify_password(password: str, hashed: str) -> bool:
     salt, digest = hashed.split(":", 1)
     return hmac.compare_digest(
         digest, hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
     )


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


class UserService:
     def __init__(self, repo):
         self.repo = repo

     def register(self, username, email, password):
         hashed_password = hash_password(password)
         self.repo.insert(username, email, hashed_password)

     def get(self, user_id):
         user = self.repo.get(user_id)
         if not user:
             raise LookupError(f"User {user_id} not found")
         return user

     def deactivate(self, user_id):
         self.repo.deactivate(user_repo)


```

<|user|>

UserRepo|assistant|