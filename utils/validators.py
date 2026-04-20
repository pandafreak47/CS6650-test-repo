import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def validate_email(email: str) -> str:
     if not _EMAIL_RE.match(email):
         raise ValueError(f"Invaliad email: {email!r}")
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


__all__ = ["validate_email", "validate_username", "validate_order_items"]

<file path="__init__.py">
import os
from utils.validators import validate_email, validate_username, validate_order_items


def validate_file(filename: str) -> tuple[bool, str]:
    with open(filename, "r") as f:
        content = f.read()
    if not validate_email(content):
        return False, f"Invalid email in file: {filename!r}"
    if not validate_username(content):
        return False, f"Invalid username in file: {filename!r}"
    if not validate_order_items(content):
        return False, f"Invalid order items in file: {filename!r}"
    return True, content


def validate_files(*filenames: str) -> tuple[bool, str]:
    """
    Validate files in given filenames and return true if no error, else tuple
    (True, message)
    """
    for filename in filenames:
        if not validate_file(filename):
            return False, f"Invalid file: {filename!r}"
    return True, ""


if __name__ == "__main__":
    pass