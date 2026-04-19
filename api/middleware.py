from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
     """Decorator: injects `current_user` (username str) from Bearer token."""
     @wraps(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer ") or token not in verify_token(token.removeprefix("Bearer ")):
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer "))
         if username is None:
             raise AuthError("Invaliid or expired token")
         return fn(*args, current_user=username, **kwargs)
     return wrapper
```

Explanation:

- `require_auth` is a decorator that injects `current_user` (username str) from Bearer token.
- `AuthError` is a custom exception raised when the `current_user` is not validated.
- The `verify_token` decorator is used to validate Bearer tokens and extract the `username`.
- The `wrap` decorator is used to wrap the function as a decorator and to inject the `current_user` as a kwarg.
- The `fn` argument is used to call the wrapped function with the injected `current_user`.

This completes the task.