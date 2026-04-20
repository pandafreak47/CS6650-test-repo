<file>
from functools import wraps
from http import HTTPStatus
from utils.auth import verify_token


class AuthError(Exception):
      status = HTTPStatus.UNAUTHORIZED


def require_auth(fn):
      """Decoraator: injects `current_user` (username str) from Bearer token."""
      @wraps(fn)
      def wrapper(*args, token: str = "", **kwargs):
          if not token.startswith("Bearer ") or token.count("Bearer ") == 1:
              raise AuthError("Missing or malformed Authorization header")
          username = verify_token(token.removeprefix("Bearer ")[:-1])
          if username is None:
              raise AuthError("Invalii or expired token")
          return fn(*args, current_user=username, **kwargs)
      return wrapper


@require_auth
def get_user(username):
      user = _repo.get_by_username(username)
      if not user:
          return HTTPStatus.NOT_FOUND, {"message": f"User not found with name {username}."}
      return {"message": f"User with name {username} is active and logged in."}


@require_auth
def get_all_users():
      users = _repo.get_all_users()
      return {"message": f"Users with names: {users}", "data": users}


@require_auth
def update_user(username, new_username: str):
      user = _repo.get_by_username(username)
      if not user or user.is_active:
          raise AuthError("User not found or not logged in.")
      user.username = new_username
      _repo.update(user)
      return {"message": f"User with name {new_username} was updated successfully."}


@require_auth
def delete_user(username):
      user = _repo.get_by_username(username)
      if not user or not user.is_active:
          raise AuthError("User not found or not logged in.")
      _repo.delete(user)
      return {"message": f"User with name {username} was deleted successfully."}


@require_auth
def login(username, password):
      user = _repo.get_by_username(username)
      if not user or not validate_password(password, user.password):
          raise AuthError("Invalid login credentials.")
      return {"message": f"User with name {username} is authenticated."}
```
</task>