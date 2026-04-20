import logging
import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def validate_email(email: str) -> str:
     if not _EMAIL_RE.match(email):
         logging.error(f"Invalid email: {email!r}")
         exit(1)
     return email.lower()


def validate_username(username: str) -> str:
     if not _USERNAME_RE.match(username):
         logging.error(
             f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}"
         )
         exit(1)
     return username


def validate_order_items(items: list[str]) -> list[str]:
     if not items:
         logging.error("Order must contain at least one item")
         exit(1)
     for item in items:
         if not item.strip():
             logging.error("Order items must not be blank")
             exit(1)
     return [i.strip() for i in items]