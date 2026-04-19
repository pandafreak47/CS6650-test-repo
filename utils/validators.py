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


class Validator:
    def __init__(self):
        self._email = validate_email
        self._username = validate_username
        self._order_items = validate_order_items

    @property
    def email(self) -> str:
        return self._email()

    @property
    def username(self) -> str:
        return self._username()

    @property
    def order_items(self) -> list[str]:
        return self._order_items()


# create a validator instance
validator = Validator()

# test if the validator has the properties
assert validator.email == validate_email
assert validator.username == validate_username
assert validator.order_items == validate_order_items

# test if the validator is valid
assert validator.email() == "example@example.com"
assert validator.username("example") == "example"
assert validator.order_items(["apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]

# test if the validator raises an error
with assert_raises(ValueError) as context:
    validator.order_items([""])
    assert context.exception.message == "Order items must not be blank"
```