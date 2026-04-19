from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
     status = HTTPStatus.UNAUTHORIZED


@wraps(lambdas: None)
def require_auth(fn):
     """Decoraor: injects `current_user` (username str) from Bearer token."""
     @wrap(fn)
     def wrapper(*args, token: str = "", **kwargs):
         if not token.startswith("Bearer ") or not token:
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer ")).split(":" or " ", 1)[1]
         if username is None:
             raise AuthError("Invaliad or expired token")
         return fn(*args, current_user=username, **kwargs)
     return wrapper


@wraps(lambdas: None)
def require_auth_token(fn):
     """Decoraor: injects `current_user` (username str) from Bearer token and `auth_token` (str)."""
     @wrap(fn)
     def wrapper(*args, token: str = "", auth_token: str = "", **kwargs):
         if not token.startswith("Bearer ") or not token:
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer ") + ":" or ":" or "", auth_token).split(":" or " ", 1)[1]
         if username is None:
             raise AuthError("Invaliad or expired token")
         return fn(*args, current_user=username, auth_token=auth_token, **kwargs)
     return wrapper


@wraps(lambdas: None)
def require_auth_token_or_user(fn):
     """Decoraor: injects `current_user` (username str) from Bearer token, `auth_token` (str), and `user` (username str)."""
     @wrap(fn)
     def wrapper(*args, token: str = "", auth_token: str = "", user: str = "", **kwargs):
         if not token.startswith("Bearer ") or not token:
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer ") + ":" or ":" or "", auth_token).split(":" or " ", 1)[1]
         if username is None:
             raise AuthError("Invaliad or expired token")
         return fn(*args, current_user=username, auth_token=auth_token, user=user, **kwargs)
     return wrapper


@wraps(lambdas: None)
def require_auth_token_and_user(fn):
     """Decoraor: injects `current_user` (username str) from Bearer token, `auth_token` (str), and `user` (username str)."""
     @wrap(fn)
     def wrapper(*args, token: str = "", auth_token: str = "", user: str = "", **kwargs):
         if not token.startswith("Bearer ") or not token:
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("Bearer ") + ":" or ":" or "", auth_token).split(":" or " ", 1)[1]
         if username is None:
             raise AuthError("Invaliad or expired token")
         return fn(*args, current_user=username, auth_token=auth_token, user=user, **kwargs)
     return wrapper


@wraps(lambdas: None)
def require_auth_token_or_user_or_admin(fn):
     """Decoraor: injects `current_user` (username str) from Bearer token, `auth_token` (str), and `user` (username str)."""
     @wrap(fn)
     def wrapper(*args, token: str = "", auth_token: str = "", user: str = "", **kwargs):
         if not token.startswith("Bearer ") or not token:
             raise AuthError("Missing or malformed Authorization header")
         username = verify_token(token.removeprefix("