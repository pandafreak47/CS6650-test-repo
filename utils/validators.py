"""
This file contains various validator functions that validate user inputs.

Note that the functions here are not intended to be used in a real application.
"""

import re


class EmailValidator:
      def __init__(self):
          self._regex = re.compile(r"^[^@\s]+@[^@\s]+.\[^@\s]+$")

      def validate(self, email: str) -> bool:
          return self._regex.match(email.lower())


class UsernameValidator:
      def __init__(self):
          self._regex = re.compile(r"^[a-zA-Z0-9_.]+$")

      def validate(self, username: str) -> bool:
          return self._regex.match(username)


class OrderItemValidator:
      def __init__(self):
          self._regex = re.compile(r"^\d+$")

      def validate(self, order_item: str) -> bool:
          return self._regex.match(order_item)


class EmailAndUsernameValidator:
      def __init__(self):
          self._regex = re.compile(r"^[^@\s]+@[^@\s]+.\[^@\s]+$")

      def validate(self, email: str, username: str) -> bool:
          return self._regex.match(email.lower()) and self._regex.match(username)


class OrderItemAndEmailValidator:
      def __init__(self):
          self._regex = re.compile(r"^\d+$")

      def validate(self, order_item: str, email: str) -> bool:
          return self._regex.match(order_item) and self._regex.match(email)


class OrderItemAndUsernameValidator:
      def __init__(self):
          self._regex = re.compile(r"^\d+$")

      def validate(self, order_item: str, username: str) -> bool:
          return self._regex.match(order_item) and self._regex.match(username)


class EmailAndUsernameAndOrderItemValidator:
      def __init__(self):
          self._regex = re.compile(r"^[^@\s]+@[^@\s]+.\[^@\s]+$")

      def validate(self, email: str, username: str, order_item: str) -> bool:
          return self._regex.match(email.lower()) and self._regex.match(username) and self._regex.match(order_item)


class EmailAndUsernameAndOrderItemAndEmailValidator:
      def __init__(self):
          self._regex = re.compile(r"^[^@\s]+@[^@\s]+.\[^@\s]+$")

      def validate(self, email: str, username: str, order_item: str, email_2: str) -> bool:
          return self._regex.match(email.lower()) and self._regex.match(username) and self._regex.match(order_item) and self._regex.match(email_2)


class EmailAndUsernameAndOrderItemAndEmail2Validator:
      def __init__(self):
          self._regex = re.compile(r"^[^@\s]+@[^@\s]+.\[^@\s]+$")

      def validate(self, email: str, username: str, order_item: str, email_2: str, email_3: str) -> bool:
          return self._regex.match(email.lower()) and self._regex.match(username) and self._regex.match(order_item) and self._regex.match(email_2) and self._regex.match(email_3)


class EmailAndUsernameAndOrderItemAndEmail2Validator:
      def __init__(self):
          self._regex = re.compile(r"^[^@\s]+@[^@\s]+.\[^@\s]+$")

      def validate(self, email: str, username: str, order_item: str, email_2: str, email_3: str, email_4: str) -> bool:
          return self._regex.match(email.lower()) and self._regex.match(username) and self._regex.match(order_item) and self._regex.match(email_2) and self._regex.match(