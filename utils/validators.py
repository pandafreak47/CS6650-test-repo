from typing import Optional, List, Callable, Union
from abc import ABCMeta, abstractmethod


class Validator(metaclass=ABCMeta):
    @abstractmethod
    def validate_order_items(self, items: List[str]) -> List[str]:
        pass

    @abstractmethod
    def validate_username(self, username: str) -> str:
        pass

    @abstractmethod
    def validate_email(self, email: str) -> str:
        pass


class EmailValidator(Validator):
    def __init__(self):
        self.email_regex = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def validate_email(self, email: str):
        if not self.email_regex.match(email):
            raise ValueError(f"Invalid email: {email!r}")
        return email.lower()


class UsernameValidator(Validator):
    def __init__(self):
        self.username_regex = re.compile(r"^[a-zA-Z0-9_]{3,32}$")

    def validate_username(self, username: str):
        if not self.username_regex.match(username):
            raise ValueError(
                f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}"
            )
        return username


class OrderValidator(Validator):
    def __init__(self):
        self.items: List[str] = []

    def add_item(self, item: str):
        self.items.append(item)

    def validate_order_items(self, items: List[str]):
        if not items:
            raise ValueError("Order must contain at least one item")
        for item in items:
            if not item.strip():
                raise ValueError("Order items must not be blank")
        return items


class ValidationError(Exception):
    pass


class ValidatorTask(object):
    def __init__(self, validator: Validator):
        self.validator = validator

    def validate(self, value: any) -> any:
        return self.validator.validate_order_items(value)


class ValidationTaskWithTask(object):
    def __init__(self, task: ValidatorTask):
        self.task = task

    def validate(self, value: any) -> any:
        return self.task.validate(value)


def validate_email_with_task(email: str) -> str:
    email_validator = EmailValidator()
    return email_validator.validate_email(email)


def validate_username_with_task(username: str) -> str:
    username_validator = UsernameValidator()
    return username_validator.validate_username(username)


def validate_order_items_with_task(items: list[str]) -> list[str]:
    order_validator = ValidatorTask(OrderValidator())
    return order_validator.validate_order_items(items)


def validate_username_with_task(username: str) -> str:
    username_validator = UsernameValidator()
    return username_validator.validate_username(username)


def validate_email_with_task(email: str) -> str:
    email_validator = EmailValidator()
    return email_validator.validate_email(email)


def validate_order_items_with_task(items: list[str]) -> list[str]:
    order_validator = ValidatorTask(OrderValidator())
    return order_validator.validate_order_items(items)


def validate_username_with_task(username: str) -> str:
    username_validator = UsernameValidator()
    return username_validator.validate_username(username)


def validate_email_with_task(email: str) -> str:
    email_validator = EmailValidator()
    return email_validator.validate_email(email)


def validate_order_items_with_task(items: list[str]) -> list[str]:
    order_validator = ValidatorTask(OrderValidator())
    return order_validator.validate_order_items(items)


def validate