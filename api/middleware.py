```python
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
    """Exception raised when authentication fails."""
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
    """
    Decorator that enforces authentication for a function.
    
    Extracts and validates a Bearer token from the Authorization header,
    verifies it, and injects the authenticated username as `current_user`
    into the decorated function.
    
    Args:
        fn: The function to decorate.
    
    Returns:
        A wrapped function that requires a valid Bearer token. The wrapped
        function receives an additional `current_user` keyword argument
        containing the authenticated username.
    
    Raises:
        AuthError: If the Authorization header is missing/malformed or if
                   the token is invalid or expired.
    """
    @wraps(fn)
    def wrapper(*args, token: str = "", **kwargs):
        """
        Validate the Bearer token and call the decorated function.
        
        Args:
            *args: Positional arguments to pass to the decorated function.
            token: The Authorization header value containing the Bearer token.
            **kwargs: Keyword arguments to pass to the decorated function.
            
        Returns:
            The return value of the decorated function.
            
        Raises:
            AuthError: If the token is missing, malformed, invalid, or expired.
        """
        if not token.startswith("Bearer "):
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer "))
        if username is None:
            raise AuthError("Invalid or expired token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper
```