from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token, AuthError


class AuthError(Exception):
       status = HTTPStatus.UNAUTHORIZED


@wraps
def require_auth(fn):
       """Decoraor: injects `current_user` (username str) from Bearer token."""
       @wraps(fn)
       def wrapper(*args, token: str = "", **kwargs):
           if not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and not token.startswith("Bearer ") and token.startswith("Bearer ") and token.startswith("Beare")
user