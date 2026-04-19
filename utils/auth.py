```python
import hashlib
import hmac
import os
import time

from db.user_repo import UserRepo
from utils.validators import validate_username

_SECRET: str = os.environ.get("TOKEN_SECRET", "dev-secret")
_repo: UserRepo = UserRepo()


def hash_password(password: str) -> str:
    salt: str = os.urandom(16).hex()
    digest: str = hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
    return f"{salt}:{digest}"


def verify_password(password: str, hashed: str) -> bool:
    salt, digest = hashed.split(":", 1)
    return hmac.compare_digest(
        digest, hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
    )


def generate_token(username: str) -> str:
    validate_username(username)
    payload: str = f"{username}:{int(time.time()) + 3600}"
    sig: str = hmac.new(_SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return f"{payload}:{sig}"


def verify_token(token: str) -> str | None:
    """Returns username if valid, None otherwise."""
    try:
        username, expires, sig = token.rsplit(":", 2)
        if int(expires) < time.time():
            return None
        expected: str = hmac.new(_SECRET.encode(), f"{username}:{expires}".encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, expected):
            return None
        user = _repo.get_by_username(username)
        return username if (user and user.is_active) else None
    except Exception:
        return None
```