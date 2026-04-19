import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


class Validator:
    def __init__(self, email=None, username=None):
        self.email = email or _EMAIL_RE
        self.username = username or _USERNAME_RE

    @property
    def email(self):
        return self.email()

    @property
    def username(self):
        return self.username()

    @property
    def order_items(self):
        return self._order_items()


# create a validator instance
validator = Validator()

# test if the validator has the properties
assert validator.email == validate_email
assert validator.username == validate_username

# test if the validator is valid
assert validator.email() == "example@example.com"
assert validator.username("example") == "example"
assert validator.order_items([["apple", "banana", "cherry"]]) == ["apple", "banana", "cherry"]

# test if the validator raise an error
with assert_raise(ValueError) as context:
    validator.order_items([""])
    assert context.exception.message == "Order items must not be blank"
```
</task>