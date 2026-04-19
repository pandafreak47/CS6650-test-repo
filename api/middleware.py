```python
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token
from utils.validators import validate_username


class AuthError(Exception):
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
    """Decorator: injects `current_user` (username str) from Bearer token."""
    @wraps(fn)
    def wrapper(*args, token: str = "", **kwargs):
        # Input validation for token parameter
        if not isinstance(token, str):
            raise AuthError("Authorization header must be a string")
        if not token:
            raise AuthError("Missing or malformed Authorization header")
        if not token.startswith("Bearer "):
            raise AuthError("Missing or malformed Authorization header")
        
        token_value = token[7:]  # Remove "Bearer " prefix
        
        # Validate token_value
        if not isinstance(token_value, str) or not token_value:
            raise AuthError("Missing or malformed Authorization header")
        if len(token_value) > 1000:
            raise AuthError("Token is too long")
        if not all(c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:." for c in token_value):
            raise AuthError("Invalid token format")
        
        username = verify_token(token_value)
        if username is None:
            raise AuthError("Invalid or expired token")
        
        # Validate username from token
        try:
            validate_username(username)
        except ValueError as e:
            raise AuthError(f"Invalid username: {str(e)}")
        
        return fn(*args, current_user=username, **kwargs)
    return wrapper
```