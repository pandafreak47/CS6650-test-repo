```python
import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def validate_email(email: str) -> str:
    """
    Validate and normalize an email address.
    
    Args:
        email: The email address to validate.
    
    Returns:
        The email address in lowercase.
    
    Raises:
        ValueError: If the email format is invalid.
    """
    if not _EMAIL_RE.match(email):
        raise ValueError(f"Invalid email: {email!r}")
    return email.lower()


def validate_username(username: str) -> str:
    """
    Validate a username.
    
    Args:
        username: The username to validate.
    
    Returns:
        The validated username.
    
    Raises:
        ValueError: If the username is not 3-32 characters long or contains invalid characters.
    """
    if not _USERNAME_RE.match(username):
        raise ValueError(
            f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}"
        )
    return username


def validate_order_items(items: list[str]) -> list[str]:
    """
    Validate and normalize a list of order items.
    
    Args:
        items: A list of item strings to validate.
    
    Returns:
        A list of stripped item strings.
    
    Raises:
        ValueError: If the list is empty or contains blank items.
    """
    if not items:
        raise ValueError("Order must contain at least one item")
    for item in items:
        if not item.strip():
            raise ValueError("Order items must not be blank")
    return [i.strip() for i in items]
```