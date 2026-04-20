from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
       status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
       """Decoraator: injects `current_user` (username str) from Bearer token."""
       @wraps(fn)
       def wrapper(*args, token: str = "", **kwargs):
           if not token.startswith("Bearer ") or token.startswith("Bearer "):
               raise AuthError("Missing or malformed Authorization header")
           username = verify_token(token.removeprefix("Bearer ")
           if username is None:
               raise AuthError("Invali<|user|> token")
           return fn(*args, current_user=username, **kwargs)
       return wrapper


@require_auth
def get_user(auth: str) -> dict:
    """Get user information by auth token."""
    return {"user_id": auth}


@require_auth
def get_token(auth: str) -> dict:
    """Get Bearer token from auth token."""
    return {"token": auth}


@require_auth
def get_all_users(auth: str) -> list:
    """Get all users (incl. Admin) info by auth token."""
    return get_users(auth)


@require_auth
def get_users(auth: str) -> list:
    """Get all users (incl. Admin) info by auth token."""
    return get_users_with_roles(auth)


@require_auth
def create_user(username: str, password: str, admin: bool) -> dict:
    """Create new user by admin flag."""
    if admin:
        raise NotImplementedError
    return {"user_id": username}


@require_auth
def update_user(user_id: str, username: str, password: str):
    """Update user by ID and admin flag."""
    if username == user_id:
        raise NotImplementedError
    return {"user_id": username}


@require_auth
def delete_user(user_id: str):
    """Delete user by ID."""
    return {"user_id": user_id}


@require_auth
def update_user_roles(user_id: str, roles: list):
    """Update user's roles."""
    return {"user_id": user_id, "roles": roles}


@require_auth
def get_all_roles(user_id: str) -> dict:
    """Get all user's roles (incl. Admin)."""
    return get_user_roles(user_id)


@require_auth
def update_user_role(user_id: str, role_id: str):
    """Update user's role."""
    return {"user_id": user_id, "role_id": role_id}


@require_auth
def get_all_roles_with_user_id(user_id: str) -> list:
    """Get all user's roles (incl. Admin) with user ID."""
    return get_user_roles_with_user(user_id)


@require_auth
def get_all_roles_with_user_ids(user_ids: list) -> list:
    """Get all user's roles (incl. Admin) with user ID(s)."""
    return get_user_roles_with_user_ids(user_ids)


@require_auth
def get_all_roles_with_admin(admin: bool) -> list:
    """Get all user's roles (incl. Admin) with admin flag."""
    return get_all_roles_with_user_ids(list(map(lambda x: x.id, get_roles_with_admin(admin))))


@require_auth
def get_roles_with_user_ids(user_ids: list) -> dict:
    """Get all user's roles (incl. Admin) with user ID(s)."""
    return {"roles": get_roles_with_user_ids(user_ids)}


@require