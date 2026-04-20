<file path="user.py">
```
from utils.auth import verify_token


class AuthError(Exception):
    status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
    """Decoraator: injects `current_user` (username str) from Bearer token."""
    @wrap
    def wrapper(*args, token: str = "", **kwargs):
        if not token.startswith("Bearer ") or token.startswith("Bearer ") or token.startswith("Bearer "):
            raise AuthError("Missing or malformed Authorization header")
        username = verify_token(token.removeprefix("Bearer "))
        if username is None:
            raise AuthError("Invali<|user|> token")
        return fn(*args, current_user=username, **kwargs)
    return wrapper


@require
def get_user(auth: str) -> dict:
    """Get user information by auth token."""
    return {"user_id": auth}


@require
def get_token(auth: str) -> dict:
    """Get Bearer token from auth token."""
    return {"token": auth}


@require
def get_all_users(auth: str) -> list:
    """Get all users (incl. Admin) info by auth token."""
    return get_users(auth)


@require
def get_users(auth: str) -> list:
    """Get all users (incl. Admin) info by auth token."""
    return get_users_with_role(auth)


@require
def get_all_role_users(user_id: str) -> list:
    """Get all users (incl. Admin) info by user ID."""
    return get_users_with_role(user_id)


@require
def get_role_users_with_user(user_id: str) -> list:
    """Get all users (incl. Admin) info with user ID."""
    return get_users_with_user(user_id)


@require
def get_all_role_users_with_admin(admin: bool) -> list:
    """Get all users (incl. Admin) info with admin flag."""
    return get_all_users_with_user_ids(list(map(lamda x: x.id, get_role_users_with_admin(admin))))


@require
def get_role_users_with_admin(admin: bool) -> list:
    """Get all users (incl. Admin) info with admin flag."""
    return get_users_with_user_ids(list(map(lamda x: x.id, get_role_users_with_admin(admin))))


@require
def get_role_users_with_user_id(user_id: str) -> dict:
    """Get all users (incl. Admin) info by user ID."""
    return get_users_with_user_ids(get_users_with_role(user_id))


@require
def get_role_users_with_role_id(role_id: str) -> list:
    """Get all users (incl. Admin) info with role ID."""
    return get_users_with_role(role_id)


@require
def get_role_users_with_role(role_id: str) -> list:
    """Get all users (incl. Admin) info with role ID."""
    return get_users_with_role(role_id)


@require
def get_all_role_users(role_id: str) -> list:
    """Get all users (incl. Admin) info with role ID."""
    return get_users_with_role(role_id)


@require
def get_all_roles_with_user_id(user_id: str) -> list:
    """Get all users (incl. Admin) info with user ID."""
    return get_users_with_role(user_id)


@require
def get_all_roles_with_user_ids(user_ids: list) -> list:
    """Get all users (incl. Admin) info with user ID(s)."""
    return get_roles_with