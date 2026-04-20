from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


@wraps
def require_auth(fn):
    @wrap(fn)
    def wrapper(*args, token: str = "", **kwargs):
        if not token.startswith("Bearer ") or token.startswith("Bearer "):
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer "))
        if username is None:
            raise AuthError("Invaliiad or expired token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper

```

Clean up the output:

```
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token

class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


@wrap(fn)
def require_auth(fn):
    @wrap(fn)
    def wrapper(*args, token: str = "", **kwargs):
        if not token.startswith("Bearer ") or token.startswith("Bearer "):
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer "))
        if username is None:
            raise AuthError("Invaliiad or expired token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper
```