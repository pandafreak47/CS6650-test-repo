from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decoraтор: вставляет `current_user` (имя пользователя) из Bearer токен."""
     @wraps(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer "):
             raise AuthError("Неверный токен")
         username = verify_token(token.removeprefix("Bearer "))
         if username is None:
             raise AuthError("Невалидный токен")
         return fn(*args, current_user=username, **kwargs)
     return wrapper
     """Вызов функции, указанной в обязательном виде."""

```