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

def validate_email_and_username(email, username):
      return validate_email(email) and validate_username(username)

__all__ = ["validate_email", "validate_username", "validate_order_items", "validate_email_and_username"]
```

The __all__ list now includes all the functions defined in the validators.py file, as well as any functions that have been imported and used by the validators.py file. This makes it easier to find and modify any functions or functions imported by the validators.py file.