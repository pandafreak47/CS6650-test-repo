<file>
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decoraator: injects `current_user` (username str) from Bearer token."""
     @wraps(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer ") or token.count("Bearer ") == 1:
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer ")[:-1])
         if username is None:
             raise AuthError("Invalii or expired token")
         return fn(*args, current_user=username, **kwargs)
     return wrapper