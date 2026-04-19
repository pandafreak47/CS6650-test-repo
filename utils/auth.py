```python
import hashlib
import hmac
import os
import time

from db.user_repo import UserRepo
from utils.validators import validate_username

_SECRET = os.environ.get("TOKEN_SECRET", "dev-secret")
_repo = UserRepo()


def hash_password(password: str) -> str:
    """
    Hash a password using SHA256 with a random salt.
    
    Args:
        password: The plaintext password to hash.
        
    Returns:
        A string in format "salt:digest" where salt is hex-encoded and digest is the SHA256 hash.
    """
    salt = os.urandom(16).hex()
    digest = hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
    return f"{salt}:{digest}"


def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a plaintext password against a hashed password.
    
    Args:
        password: The plaintext password to verify.
        hashed: The hashed password string in format "salt:digest".
        
    Returns:
        True if the password matches the hash, False otherwise.
    """
    salt, digest = hashed.split(":", 1)
    return hmac.compare_digest(
        digest, hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
    )


def generate_token(username: str) -> str:
    """
    Generate a signed authentication token for a user.
    
    Args:
        username: The username to encode in the token. Must pass username validation.
        
    Returns:
        A signed token string in format "username:expires:signature" valid for 1 hour.
        
    Raises:
        ValueError: If username fails validation.
    """
    validate_username(username)
    payload = f"{username}:{int(time.time()) + 3600}"
    sig = hmac.new(_SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return f"{payload}:{sig}"


def verify_token(token: str) -> str | None:
    """
    Verify an authentication token and return the username if valid.
    
    Args:
        token: The signed token string to verify.
        
    Returns:
        The username if the token is valid and the user is active, None otherwise.
        Returns None if the token is expired, tampered with, or the user doesn't exist or is inactive.
    """
    try:
        username, expires, sig = token.rsplit(":", 2)
        if int(expires) < time.time():
            return None
        expected = hmac.new(_SECRET.encode(), f"{username}:{expires}".encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, expected):
            return None
        user = _repo.get_by_username(username)
        return username if (user and user.is_active) else None
    except Exception:
        return None
```