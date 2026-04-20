from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     """Decoraтор: вставляет `current_user` (имя пользователя) из Bearer токена."""
     status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decoraтор: указывает `current_user` из Bearer токена."""
     @wraps(fn)
     def wrapper(*args, token: str = "", **kwargs):
          if not token.startswith("Bearer ") or token.startswith("Bearer ", token.count(" ")):
               raise AuthError("Неверный токен")
          username = verify_token(token.removeprefix("Bearer ") or token.replace("Bearer ", "").strip())
          if username is None:
               raise AuthError("Невалидный токен")
          return fn(*args, current_user=username, **kwargs)
     return wrapper

```
</task>