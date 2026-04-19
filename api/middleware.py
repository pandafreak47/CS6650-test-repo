```python
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
    """Exception raised when authentication fails.
    
    Attributes:
        status: HTTP status code for the error (401 Unauthorized).
    """
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
    """Decorator that enforces authentication and injects the current user.
    
    Extracts and verifies a Bearer token from the Authorization header,
    validates it using verify_token, and injects the authenticated username
    as the `current_user` parameter to the decorated function.
    
    Args:
        fn: The function to decorate.
    
    Returns:
        A wrapper function that checks authentication before calling the
        original function.
    
    Raises:
        AuthError: If the Authorization header is missing, malformed,
            or contains an invalid or expired token.
    """
    @wraps(fn)
    def wrapper(*args, token: str = "", **kwargs):
        """Verify Bearer token and call the decorated function with current_user.
        
        Args:
            *args: Positional arguments to pass to the decorated function.
            token: The Authorization header value containing the Bearer token.
            **kwargs: Keyword arguments to pass to the decorated function.
        
        Returns:
            The return value of the decorated function.
        
        Raises:
            AuthError: If the Authorization header is missing, malformed,
                or contains an invalid or expired token.
        """
        if not token.startswith("Bearer "):
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer "))
        if username is None:
            raise AuthError("Invalid or expired token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper
```