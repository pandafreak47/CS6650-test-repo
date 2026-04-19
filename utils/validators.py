```python
import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def validate_email(email: str) -> str:
    if not _EMAIL_RE.match(email):
        raise ValueError(f"Invalid email: {email!r}")
    return email.lower()


def validate_username(username: str) -> str:
    if not _USERNAME_RE.match(username):
        raise ValueError(
            f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}"
        )
    return username


def validate_order_items(items: list[str]) -> list[str]:
    if not items:
        raise ValueError("Order must contain at least one item")
    for item in items:
        if not item.strip():
            raise ValueError("Order items must not be blank")
    return [i.strip() for i in items]
```