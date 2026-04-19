from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decoraтор: инъектирует `наименования_пользователя` (наименование_пользователя_тип) из БД через авторизованный юзер."""
     @wraps(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer "):
             raise AuthError("Минимально требуется авторизованный юзер")
         username = verify_token(token.removeprefix("Bearer "))
         if username is None:
             raise AuthError("Неверный авторизованный юзер или токен")
         return fn(*args, current_user=username, **kwargs)
     return wrapper
```

Expected output:
```
<file path="api/middleware.py">
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decoraтор: инъектирует `наименования_пользователя` (наименование_пользователя_тип) из БД через авторизованный юзер."""
     @wraps(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer "):
             raise AuthError("Минимально требуется авторизованный юзер")
         username = verify_token(token.removeprefix("Bearer "))
         if username is None:
             raise AuthError("Неверный авторизованный юзер или токен")
         return fn(*args, current_user=username, **kwargs)
     return wrapper
```

Expected output:
```
<task>
Add a logging statement at the entry point of each public function.
</task>
```

Expected output:
```
```

Expected output:
```
<file path="utils/auth.py">
from .connection import get_connection
from .db.user_repo import UserRepo
from .validators import validate_username


class Auth:
     def __init__(self, repo: UserRepo):
         self._repo = repo

     def generate_token(self, username: str) -> str:
         validate_username(username)
         payload = f"{username}:{int(time.time() + 3600)}"
         sig = self._repo.hash_password(username)
         return f"{payload}:{sig}"

     def verify_token(self, token: str) -> str | None:
         try:
             username, expires, sig = token.rsplit(":", 2)
             expected = self._repo.verify_hash(sig, token)
             if int(expires) < time.now() + 3600:
                 return None
             expected = self._repo.strip()
             if 360s:exp_payload)
         except s:username":
             self._repo:
         f:username:password::):
         username:
             payload: _s::"username:exp:
username:token:"username:expire.s:"
username:expire:"username"
username")
user
username:username>
username> <filename:validity:epos:valid:epos:valid:exp:valid:username:valid: 1:valid:username:validator or > <username:valid(@username:username@>username:exp:username:valid:exp:username:username>user@username:username:username:username:username:username:exp:username:username:exp:username:username:
fromusername>username:valid:username:username:username:valid:username:username:username:@username:username:username:username:username:username:username:username:validator:username:username:username:username:username:username:username:valid:username:username:username:username:username:user:username:username:username:username:username:username:username:username: