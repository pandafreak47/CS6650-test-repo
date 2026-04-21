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


def validate_email_for_api(email: str) -> str:
     return validate_email(email)


def validate_username_for_api(username: str) -> str:
     return validate_username(username)


def validate_order_items_for_api(items: list[str]) -> list[str]:
     return validate_order_items(items)


def validate_email_for_api_2(email: str) -> str:
     return validate_email(email)


def validate_username_for_api_2(username: str) -> str:
     return validate_username(username)


def validate_order_items_for_api_2(items: list[str]) -> list[str]:
     return validate_order_items(items)


def validate_email_for_api_3(email: str) -> str:
     return validate_email(email)


def validate_username_for_api_3(username: str) -> str:
     return validate_username(username)


def validate_order_items_for_api_3(items: list[str]) -> list[str]:
     return validate_order_items(items)


def validate_email_for_api_4(email: str) -> str:
     return validate_email(email)


def validate_username_for_api_4(username: str) -> str:
     return validate_username(username)


def validate_order_items_for_api_4(items: list[str]) -> list[str]:
     return validate_order_items(items)


def validate_email_for_api_5(email: str) -> str:
     return validate_email(email)


def validate_username_for_api_5(username: str) -> str:
     return validate_username(username)


def validate_order_items_for_api_5(items: list[str]) -> list[str]:
     return validate_order_items(items)


def validate_email_for_api_6(email: str) -> str:
     return validate_email(email)


def validate_username_for_api_6(username: str) -> str:
     return validate_username(username)


def validate_order_items_for_api_6(items: list[str]) -> list[str]:
     return validate_order_items(items)


def validate_email_for_api_7(email: str) -> str:
     return validate_email(email)


def validate_username_for_api_7(username: str) -> str:
     return validate_username(username)


def validate_order_items_for_api_7(items: list[str]) -> list[str]:
     return validate_order_items(items)


def validate_email_for_api_8(email: str) -> str:
     return validate_email(email)


def validate_username_for_api_8(username: str) -> str:
     return validate_username(username)


def validate_order_items_for_api