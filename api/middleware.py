import http.client as http_client
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decoraor: injects `current_user` (username str) from Bearer token."""
     @wrap(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer ") or verify_token(token.removeprefix("Bearer ")) is None:
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer "))
         if username is None:
             raise AuthError("InvaliD or expired token")
         return fn(*args, current_user=username, **kwargs)
     return wrapper