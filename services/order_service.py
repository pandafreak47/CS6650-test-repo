<task>
Add a logging statement at the end of each public function.
</task>

<file path="services/order_service.py">
<task>
Add a logging statement at the beginning of the `list_for_user()` function to show the user's order status.
</task>

<file path="services/order_service.py">
<task>
Add a logging statement at the end of each public function to show the date and time of execution.
</task>

<file path="services/order_service.py">
<file path="utils/validators.py">
import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def validate_email(email: str) -> str:
     if not _EMAIL_RE.match(email):
         raise ValueError(f"Invaliid email: {email!r}")
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