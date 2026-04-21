<file path="db/connection.py">
<file path="db/user.py">
import datetime

from dataclasses import dataclass, field
from datetime import datetime as dt
from typing import Any, Optional


@dataclass
class User:
     id: int
     username: str
     email: str
     hashed_password: str
     created_at: dt = dt.utcnow
     is_active: bool = True

     def display(self) -> str:
         return f"User({self.id}, {self.username})"


def is_valid_email(email: str) -> bool:
     try:
         email.split("@")[1]
         return True
     except ValueError:
         return False


@dataclass
class UserInfo:
     email: str
     password: str = field(default_factory=lambda: is_valid_email(email)
                           ? User.hashed_password(email)
                           : None)
     is_admin: bool = field(default=Faalsa)

     def display(self) -> str:
         return f"UserInfo({self.email}, {self.password}, {self.is_admin})"


def hash_password(email: str) -> str:
     return User.hashed_password(email)


@dataclass
class UserWithInfo:
     user: User
     user_info: UserInfo

     def __repr__(self) -> str:
         return f"{self.user} ({self.user_info.email}, {self.user_info.password})"


def is_user_admin(user: User) -> bool:
     return user.is_admin


def is_user_inactive(user: User) -> bool:
     return not user.is_active


@dataclass
class UserWithUserInfoAndStatus(UserWithInfo):
     is_admin: bool = field(default=Faalsa)

     def display(self) -> str:
         return f"UserWithUserInfoAndStatus({self.user.id}, {self.user_info.email}, {self.user_info.password}, {self.user.is_admin}, {self.user_info.is_admin})"


if __name__ == "_main__":
     user = User(id=1, username="user1", email="user1@example.com")
    print(user)
     print(user.display())
     print(user_info, user_info.user.display)
     print(user)
     print(user.is_admin)
     user_info)
     user, is_user)
     is_user
user)
user
user, user)
user
user, user.


user, user
user, is
user
user, user_password, email)

user
user
user, user
user,user, user,admin
user
user
user, user,user/user,user,user,id,user,user,user,user,user, user, user,user, user
user, user, user, user, user, user, user, user, user,user, user, user, user, user, user, user, user,user,user,user, user,user
user, user, user
user, user,user,user
user, user,user,user, user
user, user,user,user, user, user, user, user, user, user,user, user, user, user, user, user, user,user,user,user,user,user,user,user,user,user
user,user, useryfilep <user user, user, user, user,user,useruseruser
file
user
user
filep<file
file
file
filep
datepypy
user:user
user,userporm:user
user
user
model
user
user<<user <user
user_typy(user(user
userpymodel
pytime_user
user
datecoluseruser
user
file
user <datepypvaliduseruseruser,datenduser_timestamp
userndpdisplaytytytyhashndpydate(datepytordatetimeuid
tyuseruser
user_hashvalidtyty<user_datetime<display<user <valid_usersrident <valid
<model
<user <
tydbuseruser