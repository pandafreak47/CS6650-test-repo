<file>
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decoraor: injects `current_user` (username str) from Bearer token."""
     @wraps(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer ") or not verify_token(token.removeprefix("Bearer ")):
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer ") or "Bearer " + token.replace("Bearer ", "")).lstrip()
         if username is None:
             raise AuthError("Invaliid or expired token")
         return fn(*args, current_user=username, **kwargs)
     return wrapper
     return wrapper
```