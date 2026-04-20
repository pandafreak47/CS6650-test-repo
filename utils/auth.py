<file path="utils/user_repo.py">
from typing import Union, Tuple, List, Optional
from typing_extensions import overload
from functools import reduce

class Auth:
    @overload
    def __init__(self, username: str, password: str) -> None:
        """
        Constructor for Auth class.
        """
        ...
    @overload
    def __init__(self, username: str, password: str, **kwargs: Any) -> None:
        """
        Constructor for Auth class with keyword arguments.
        """
        ...

    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def check(self, token: str) -> bool:
        if token != self._username:
            return False
        else:
            return True

    @property
    def user_id(self) -> Optional[int]:
        """
        Getter for user ID.
        """
        return self._user_id

    @property
    def email(self) -> Optional[str]:
        """
        Getter for email.
        """
        return self._email

    @email.setter
    def email(self, value: Optional[str]) -> None:
        """
        Setter for email.
        """
        if value is not None:
            self._email = value

    @property
    def password(self) -> Optional[str]:
        """
        Getter for password.
        """
        return self._password

    @password.setter
    def password(self, value: Optional[str]) -> None:
        """
        Setter for password.
        """
        if value is not None:
            self._password = value

    def __repr__(self) -> str:
        return f"Auth(user_id={self.user_id!r}, email={self.email!r}, password={self.password!r})"


@overload
def decode_token(token: str) -> Union[Auth, None]:
    ...


def decode_token(token: str) -> Optional[Auth]:
    return decode_token(token)


def encode_token(auth: Auth) -> str:
    return encode_token(auth)


def decode_token_for_username(username: str) -> Optional[Auth]:
    return decode_token_for_username(username)


def encode_token_for_username(auth: Auth, username: str) -> str:
    return encode_token_for_username(auth, username)


@overload
def hash_password(password: str) -> str:
    ...


def hash_password(password: str) -> str:
    return hash_password(password)


def validate_username_for_password(username: str, password: str) -> bool:
    return validate_username_for_password(username, password)


def validate_password_for_username(username: str, password: str) -> bool:
    return validate_password_for_username(username, password)


@overload
def validate_email_for_username(email: str, username: str) -> bool:
    ...


def validate_email_for_username(email: str, username: str) -> bool:
    return validate_email_for_username(email, username)


@overload
def validate_order_items(order_items: List[Dict]) -> None:
    ...


def validate_order_items(order_items: List[Dict]) -> None:
    for order_item in order_items:
        if not validate_order_items(order_item):
            raise Exception("Invalid order item")


@overload
def validate_files(filename: str) -> Tuple[bool, str]:
    ...


def validate_files(filename: str) -> Tuple[bool, str]:
    return True, filename


def validate_files_for_username(username: str, filename: str) -> Tuple[bool, str]:
    return validate_files_for_username(username, filename)


@overload
def validate_password(password: str) -> bool:
    ...


def validate_password(password: str) -> bool:
    return