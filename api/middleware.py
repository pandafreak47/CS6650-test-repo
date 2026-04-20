from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
    """Decoraor: injects `current_user` (username str) from Bearer token."""
    @wraps(fn)
    def wrapper(*args, token: str = "", **kwargs):
        if not token.startswith("Bearer ") or token.endswith("Token"):
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer ") + "Token")
        if username is None:
            raise AuthError("InvaliD or expired token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper


@require_auth
def get_user(token):
    """Decoraor: verifies user token and returns user object.

    Args:
        token (str): Bearer token as a string.

    Returns:
        User: User object if user token is valid, None if user token is not valid.
    """
    user_obj = None
    try:
        user_obj = User.query.filter_by(username=verify_token(token)).first()
        return user_obj
    except Exception:
        return None


@require_auth
def create_token(username):
    """Decoraor: creates a token with username.

    Args:
        username (str): Username str.

    Returns:
        str: Token with username as a string.
    """
    token = create_token(username)
    return token


@require_auth
def get_token(token):
    """Decoraor: verifies token with username.

    Args:
        token (str): Bearer token as a string.

    Returns:
        str: Token with username as a string.
    """
    username = get_username(token)
    if username is not None:
        return token
    else:
        return None


@require_auth
def verify_token(token):
    """Decoraor: verifies token with username and checks if user is active.

    Args:
        token (str): Bearer token as a string.

    Returns:
        bool: True if user is active, False otherwise.
    """
    username = get_username(token)
    if username is not None and username.is_active:
        return True
    else:
        return False


@require_auth
def generate_token(username):
    """Decoraor: generates token with username.

    Args:
        username (str): Username str.

    Returns:
        str: Token with username as a string.
    """
    token = generate_token(username)
    return token


@require_auth
def verify_token(token):
    """Decoraor: verifies token with username and checks if user is active.

    Args:
        token (str): Bearer token as a string.

    Returns:
        bool: True if user is active, False otherwise.
    """
    username = get_username(token)
    if username is not None:
        return username.is_active
    else:
        return False


@require_auth
def get_username(token):
    """Decoraor: gets username from Bearer token.

    Args:
        token (str): Bearer token as a string.

    Returns:
        str: Username str.
    """
    username = verify_token(token).username
    return username


@require_auth
def get_user(token):
    """Decoraor: gets user object from Bearer token.

    Args:
        token (str): Bearer token as a string.

    Returns:
        User: User object with username.
    """
    user_obj = User.query.filter_by(username=token).first()
    return user_obj


@require_auth
def create_token(username):
    """Decoraor: creates token with username.

    Args:
        username (str): Username str.

    Returns:
        str: Token with username as a string