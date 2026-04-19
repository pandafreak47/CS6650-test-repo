```python
import logging
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token

logger = logging.getLogger(__name__)


class AuthError(Exception):
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
    """Decorator: injects `current_user` (username str) from Bearer token."""
    @wraps(fn)
    def wrapper(*args, token: str = "", **kwargs):
        logger.info(f"require_auth decorator called for function: {fn.__name__}")
        if not token.startswith("Bearer "):
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer "))
        if username is None:
            raise AuthError("Invalid or expired token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper
```