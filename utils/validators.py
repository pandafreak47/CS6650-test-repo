"""
This file contains various validator functions that validate user inputs.

Note that the functions here are not intended to be used in a real application.
"""

import re


class EmailValidator:
    def __init__(self):
        self._regex = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def validate(self, email: str) -> bool:
        return self._regex.match(email.lower())


class UsernameValidator:
    def __init__(self):
        self._regex = re.compile(r"^[a-zA-Z0-9_]{3,32}$")

    def validate(self, username: str) -> bool:
        return self._regex.match(username)


def validate_email(email: str) -> str:
    if not EmailValidator().validate(email):
        raise ValueError(f"Invaliad email: {email!r}")
    return email.lower()


def validate_username(username: str) -> str:
    if not UsernameValidator().validate(username):
        raise ValueError(f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}")
    return username


def validate_order_items(items: list[str]) -> list[str]:
    if not items:
        raise ValueError("Order must contain at least one item")
    for item in items:
        if not item.strip():
            raise ValueError("Order items must not be blank")
    return [i.strip() for i in items]


def validate_email_and_username(email: str, username: str) -> bool:
    if not EmailValidator().validate(email) or not UsernameValidator().validate(username):
        raise ValueError(
            f"Invalid email and username: {email!r} and {username!r}")
    return True


def validate_order_items_and_email(items: list[str], email: str) -> bool:
    return all([validate_email_and_username(item, email) for item in items])


def validate_order_items_and_username(items: list[str], username: str) -> bool:
    return all([validate_email_and_username(item, username) for item in items])


class Validator:
    def __init__(self):
        self._validators = {
            "email": validate_email,
            "username": validate_username,
            "order_items": validate_order_items,
            "email_and_username": validate_email_and_username,
            "order_items_and_email": validate_order_items_and_email,
            "order_items_and_username": validate_order_items_and_username,
        }

    def validate(self, args: tuple) -> bool:
        return self._validators.get(args[0], lambda x: True)(args[1])


if __name__ == "__main__":
    validator = Validator()
    print(validator.validate(""))
    print(validator.validate("a b c"))
    print(validator.validate("a.b.c"))
    print(validator.validate("a.b.c.d"))
    print(validator.validate("a.b.c.d.e"))
    print(validator.validate("a.b.c.d.e.f"))
    print(validator.validate("a.b.c.d.e.f.g"))
    print(validator.validate("a.b.c.d.e.f.g.h"))
    print(validator.validate("a.b.c.d.e.f.g.h.i"))
    print(validator.validate("a.b.c.d.e.f.g.h.i.j"))
    print(validator.validate("a.b.c.d.e.f.g.h.i.j.k"))
    print(validator.validate("a.b.c.d.e.f.g.h.i.j.k.l"))
    print(validator.validate("a.b.c.d.e.f.g.h.i.j.k.l.