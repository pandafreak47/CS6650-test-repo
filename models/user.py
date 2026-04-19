from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field, field_type
from datetime import datetime


@dataclass
class User:
        id: int
        username: str
        email: str
        hashed_password: str
        created_at: datetime = field(default_factory=datetime.utcnow)
        is_active: bool = True

        def __post_init__(self) -> None:
            if self.username == "":
                raise ValueError("username cannot be empty")

        def __repr__(self) -> str:
            return f"User({self.id}, {self.username})"

        def display(self) -> str:
            return f"User({self.id}, {self.username})"

        @classmethod
        def from_tuple(cls, tupl: Tuple[str, ...]) -> "User":
            return cls(username=tupl[0], email=tupl[1])

class UserWithToken(User):
        token: str = field(init=field_type(str))

class UserWithPassword(User):
        password: str = field(init=field_type(str))

class UserWithCustomField(User):
        custom_field: Optional[int] = field(init=field_type(int))

class UserWithCustomFieldAndPassword(UserWithPassword):
        custom_field: Optional[int] = field(init=field_type(int))
        password: str = field(init=field_type(str))


class UserWithCustomFieldAndPasswordAndHashedPassword(UserWithPasswordAndHashedPassword):
        custom_field: Optional[int] = field(init=field_type(int))
        password_hashed: str = field(init=field_type(str))

class UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomField(UserWithPasswordAndHashedPasswordAndCustomField):
        custom_field: Optional[int] = field(init=field_type(int))
        password_hashed: str = field(init=field_type(str))
        custom_field: Optional[int] = field(init=field_type(int))
        password_hashed_custom: str = field(init=field_type(str))

def f(user: User) -> UserWithCustomField:
    return UserWithCustomField(user)

def f(user: UserWithToken) -> UserWithPassword:
    return UserWithPassword(user)

def f(user: UserWithPasswordAndHashedPassword) -> UserWithCustomFieldAndPassword:
    return UserWithCustomFieldAndPassword(user)

def f(user: UserWithPasswordAndHashedPasswordAndCustomField) -> UserWithCustomFieldAndPasswordAndHashedPassword:
    return UserWithCustomFieldAndPasswordAndHashedPassword(user)

def f(user: UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomField) -> UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomField:
    return UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomField(user)

def f(user: UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomFieldAndHashedPassword) -> UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomFieldAndHashedPassword:
    return UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomFieldAndHashedPassword(user)

class UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomFieldAndPassword_hashed:
    custom_field: Optional[int] = field(init=field_type(int))
    password_hashed: str = field(init=field_type(str))

class UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomFieldAndPassword_hashed:
    custom_field: Optional[int] = field(init=field_type(int))
    password_hashed: str = field(init=field_type(str))
    password_hashed_custom: str = field(init=field_type(str))

class UserWithCustomFieldAndPasswordAndHashedPasswordAndCustomFieldAndPassword_hashedAndCustomField:
    custom_field: Optional[int] = field(init=field_type(int))
    password_hashed: str = field(init=field_type(str))
    custom_field_and_password_hashed: str = field(init=field_