```python
import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def validate_email(email: str) -> str:
    if not isinstance(email, str):
        raise TypeError(f"Email must be a string, got: {type(email).__name__}")
    if not email:
        raise ValueError("Email must not be empty")
    if not _EMAIL_RE.match(email):
        raise ValueError(f"Invalid email: {email!r}")
    return email.lower()


def validate_username(username: str) -> str:
    if not isinstance(username, str):
        raise TypeError(f"Username must be a string, got: {type(username).__name__}")
    if not username:
        raise ValueError("Username must not be empty")
    if not _USERNAME_RE.match(username):
        raise ValueError(
            f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}"
        )
    return username


def validate_order_items(items: list[str]) -> list[str]:
    if not isinstance(items, list):
        raise TypeError(f"Items must be a list, got: {type(items).__name__}")
    if not items:
        raise ValueError("Order must contain at least one item")
    for item in items:
        if not isinstance(item, str):
            raise TypeError(f"Each item must be a string, got: {type(item).__name__}")
        if not item.strip():
            raise ValueError("Order items must not be blank")
    return [i.strip() for i in items]
```