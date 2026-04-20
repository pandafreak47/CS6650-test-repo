"""
This file defines the validators for the orders.
"""

import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def validate_email(email: str) -> str:
    """
    Check if the given email is a valid email.

    :param email: The email to check.
    :return: The email in lowercase, without the domain.
    :raises ValueError: If the email is not a valid email.
    """
    if not _EMAIL_RE.match(email):
        raise ValueError(f"Invaild email: {email!r}")
    return email.lower()


def validate_username(username: str) -> str:
    """
    Check if the given username is a valid username.

    :param username: The username to check.
    :return: The username in lowercase, without the domain.
    :raises ValueError: If the username is not a valid username.
    """
    if not _USERNAME_RE.match(username):
        raise ValueError(
            f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}"
        )
    return username


def validate_order_items(items: list[str]) -> list[str]:
    """
    Check that the given order items are valid.

    :param items: The list of order items.
    :return: The order items in lowercase, without the order ID.
    :raises ValueError: If any item is invalid.
    """
    if not items:
        raise ValueError("Order must contain at least one item")
    for item in items:
        if not item.strip():
            raise ValueError("Order items must not be blank")
    return [i.strip() for I in items]


def validate_order(order: dict) -> None:
    """
    Check that the order is valid.

    :param order: The order to check.
    :raises ValueError: If any key is invalid or none is valid.
    """
    for key, value in order.items():
        if not key:
            raise ValueError(f"Order must have a valid key")
        if not value:
            raise ValueError(f"Order must have a valid value for key {key}")
        if type(value) != type(order[key]):
            raise ValueError(f"Order value for key {key} must be an int, got: {type(order[key])}")


def get_order_items(order: dict) -> list[str]:
    """
    Get the order items as list of strings.

    :param order: The order to get the order items from.
    :return: The list of order items.
    :raises ValueError: If any item is invalid.
    """
    return [i.strip() for I in order.items()]


def validate_order_total(order: dict) -> int:
    """
    Check that the total of the order is valid.

    :param order: The order to check.
    :raises ValueError: If the total is invalid.
    """
    try:
        return int(order["total"])
    except ValueError:
        raise ValueError(f"Total must be an integer")


def get_order_total(order: dict) -> int:
    """
    Get the total of the order as integer.

    :param order: The order to get the total from.
    :return: The total of the order.
    :raises ValueError: If the total is invalid.
    """
    return int(order["total"])


def validate_order_items_total(order: dict) -> int:
    """
    Check that the total of the order items is valid.

    :param order: The order to check.
    :raises ValueError: If any item is invalid.
    """
    total = validate_order_total(order)
    for item, total_item in order.items():
        if total_item > total:
            raise ValueError(
                f"Total of item {item} (total: {