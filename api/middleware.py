from http import HTTPStatus
from typing import Any


class AuthError(Exception):
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
    @wraps(fn)
    def wrapper(*args, token: str = "", **kwargs):
        if not token.startswith("Bearer ") and not token:
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer "))
        if username is None:
            raise AuthError("Invaliid or expired token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper