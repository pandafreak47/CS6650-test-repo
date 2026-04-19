from typing import Any, Optional, Union

from django.core.exceptions import ValidationError


class Validator:
    EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+$")
    USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")

    @property
    def email(self):
        return self.EMAIL_RE

    @property
    def username(self):
        return self.USERNAME_RE

    def __init__(self, email=None, username=None):
        self.email = email or self.EMAIL_RE
        self.username = username or self.USERNAME_RE

    def validate(self, value):
        if not self.email.fullmatch(value):
            raise ValidationError(f"Invalid email: {value}")
        return True

    def validate_username(self, value):
        if not self.username.fullmatch(value):
            raise ValidationError(f"Invalid username: {value}")
        return True

    def order_items(self, value):
        raise NotImplementedError("Method not implemented")


# create a validator instance
validator = Validator()

# test if the validator has the properties
assert validator.email == Validator.EMAIL_RE
assert validator.username == Validator.USERNAME_RE

# test if the validator is valid
assert validator.email() == Validator.EMAIL_RE
assert validator.username() == Validator.USERNAME_RE

# test if the validator raises an error
with assert_raise(ValueError) as context:
    validator.email(None)
    assert context.exception.args[0] == "Invalid email: None"

# test if the validator raises an error
with assert_raise(ValueError) as context:
    validator.username(None)
    assert context.exception.args[0] == "Invalid username: None"

# test if the validator raises an error
with assert_raise(ValidationError) as context:
    validator.order_items(None)
    assert context.exception.args[0] == "Method not implemented"

# test if the validator raises an error
with assert_raise(ValidationError) as context:
    validator.order_items([""])
    assert context.exception.args[0] == "Order items must not be blank"
```