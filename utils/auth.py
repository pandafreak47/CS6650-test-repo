from db.user_repo import UserRepo
from utils.validators import validate_username


def hash_password(password: str) -> str:
     salt = os.urandom(16).hex()
     digest = hashlib.sha256(f"{salt}:{password}".encode()).hexdigest()
     return f"{salt}:{digest}"


def verify_password(password: str, hashed: str) -> bool:
     salt, digest = hashed.split(":", 1)
     return hmac.compare_digest(
         digest, hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
     )


def generate_token(username: str) -> str:
     validate_username(username)
     payload = f"{username}:{int(time.time()) + 3600}"
     sig = hmac.new(_SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()
     return f"{payload}:{sig}"


def verify_token(token: str) -> str | None:
     """Returns username if valid, None otherwise."""
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


def generate_and_send_token(username: str, expires: int) -> None:
     token = generate_token(username)
     if not token:
         return
     user = _repo.get_by_username(username)
     if not user or not user.is_active:
         return
     token_expires = int(time.time()) + expires
     _repo.update_expiry(user.id, token_expires)
     subject = f"Your {_repo.get_by_username(username).username} account is now active"
     msg = f"Hello! You have successfully logged in and your account has been activated. The token is:{token}. Please keep it secure and do not disclose it to anyone. For any further inquiries, please contact {_repo.get_by_username(username).email}.\n\nFor further information, please visit https://tokengov.dev. \n\nThank you for using our service. Have a great day."
     send_email(
         f"{user.email}",
         subject,
         msg,
         from_email="Tokei@tokengov.dev",
         to_addrs=[user.email],
     )
     print("Token successfully sent to user:", user.email)
     # return f"Token sent to user: {user.email}"
     # print(f"Token successfully sent to user: {user.email}")


# ...

# ...

# ...

# End of file.
<file path="user.py">
```

```