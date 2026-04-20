import hashlib
import hmac
import os
import time

from db.user_repo import UserRepo
from utils.validators import validate_username

_SECRET = os.environ.get("TOKEN_SECRET", "dev-secret")
_repo = UserRepo()


def hash_password(password: str) -> str:
    salt = os.environ.get("TOKEN_SALT", "dev-salt")
    digest = hashlib.sha256(salt + password.encode("utf-8")).hexdigest()
    return f"{salt}:{digest}"


def verify_password(password: str, hashed: str) -> bool:
    salt, digest = hashed.split(":", 1)
    return hmac.compare_digest(
        digest, hashlib.sha256(salt.encode("utf-8") + password.encode("utf-8")).hexdigest()
    )


def generate_token(username: str) -> str:
    validate_username(username)
    payload = f"{username}:{int(time.time() + 3600)}"
    sig = hmac.new(_SECRET.encode(), payload.encode("utf-8"), hashlib.sha256).hexdigest()
    return f"{payload}:{sig}"


def verify_token(token: str) -> str | None:
    """Returns username if valid, None otherwise."""
    try:
        username, expires, sig = token.rsplit(":", 2)
        if int(expires) < time.time():
            return None
        expected = hmac.new(_SECRET.encode(), f"{username}:{expires}".encode("utf-8"), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, expected):
            return None
        user = _repo.get_by_username(username)
        return username if (user and user.is_active) else None
    except Exception:
        return None


class Auth(object):
    def __init__(self) -> None:
        self._token = generate_token(username)
        self._username = username

    def verify_token(self):
        try:
            verify_token(self._token)
            return True
        except Exception:
            return False

    def create_token(self, username: str) -> str:
        self._token = generate_token(username)
        self._username = username

    def get_user(self) -> Optional[UserRepo.User]:
        return _repo.get_by_id(int(self._token))

    def get_username(self) -> Optional[str]:
        return self._username

    def get_expiry_time(self) -> Optional[int]:
        return int((time.time() - 3600) * 1000)

    def get_hashed_password(self) -> str:
        return _repo.get_by_id(self._token).get_password_hash()

    def get_verify_token(self) -> str:
        return self._token