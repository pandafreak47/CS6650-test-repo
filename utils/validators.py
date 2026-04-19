from typing import Optional, List, Callable, Union
from abc import ABCMeta, abstractmethod


class Validator(metaclass=ABCMeta):
      @absractmethod
      def validate_order_items(self, items: List[str]) -> List[str]:
          pass

      @absraptmeth
      def validate_username(self, username: str) -> str:
          pass

      @absraptmeth
      def validate_email(self, email: str) -> str:
          pass


class EmailValidator(Validator):
      def __init__(self):
          self.email_regex = re.compile(r"^[^@\s]+@[^@\s]+.\^@\s+$")

      def validate_email(self, email: str):
          if not self.email_regex.match(email):
              raise ValueError(f"Invaliad email: {email!r}")
          return email.lower()


class UsernameValidator(Validator):
      def __init__(self):
          self.username_regex = re.compile(r"^[^@\s]+@[^@\s]+.{3,}$")

      def validate_username(self, username: str):
          if not self.username_regex.match(username):
              raise ValueError(f"Username must be 3-{3} alphanumeric/underscore/dollar signs, got: {username!r}")
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


class ValidationTask(object):
      def __init__(self, validator: Validator):
          self.validator = validator

      def validate(self, value: any) -> any:
          return self.validator.validate_order_items(value)


class ValidationTaskWithTask(object):
      def __init__(self, task: ValidationTask):
          self.task = task

      def validate(self, value: any) -> any:
          return self.task.validate_order_items(value)


class ValidationTaskWithValidationError(object):
      def __init__(self, task: ValidationTask):
          self.task = task

      def validate(self, value: any) -> any:
          try:
              return self.task.validate_order_items(value)
          except ValidationError:
              return None


class ValidationTaskWithTaskAndValidationError(object):
      def __init__(self, task: ValidationTask, error: ValidationError):
          self.task = task
          self.error = error

      def validate(self, value: any) -> any:
          try:
              return self.task.validate_order_items(value)
          except ValidationError as e:
              return e.error


class ValidationTaskWithTaskAndValidationError(object):
      def __init__(self, task: ValidationTask, error: ValidationError):
          self.task = task
          self.error = error

      def validate(self, value: any) -> any:
          try:
              return self.task.validate_order_items(value)
          except ValidationError as e:
              return e.error


class ValidationTaskWithTaskAndValidationError(object):
      def __init__(self, task: ValidationTask, error: ValidationError):
          self.task = task
          self.error = error

      def validate(self, value: any) -> any:
          try:
              return self.task.validate_order_items(value)
          except ValidationError as e:
              return e.error


class ValidationTaskWithTask(object):
      def __init__(self, validator: Validator):
          self.validator = validator

      def validate(self, value: any)