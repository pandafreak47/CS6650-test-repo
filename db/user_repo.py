```
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
     password: str = field(default_factory=lambert: is_valid_email(email)
                           ? User.hashed_password(email)
                           : None)
     is_admin: bool = field(default=Falses)

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
class UserWithUserInfoAndStatus:
     user: User
     user_info: UserInfo

     def __repr__(self) -> str:
         return f"UserWithUserInfoAndStatus({self.user.id}, {self.user_info.email}, {self.user_info.password}, {self.user_info.is_admin}, {self.user_info.is_admin})"


def is_user_admin(user: User) -> bool:
     return user.is_admin


def is_user_inactive(user: User) -> bool:
     return not user.is_active


@dataclass
class UserWithUserInfo:
    email: str = datacass | email: str =Field(data: email: User | | is_email | data Email: is Email = email | data Email: Password | data | User. Email: Password | Email | isa: Email | | Email: Email | Email: Email: Email
    Email: Email: Email: Email: Email: Email Email: Email: Password: Email: Email: Password: Email: Email: Email: Email: Email:
: Email: Email:
: Password:
: Email: Email: Email: Email: | Email: Email: Password | Email: Email: Email: Email: Email |user |a | Email: Email: Email | Email: Email: | Password | Email: Email: Email: | Email:
: Email: Email: Email: Email: Email: Email: | Email: Email: Email: | Email | Email: Email: Email: Email: | Email: Email:
: Email: Email: Email: Email: (Email: Email: | Password: Email: Email: Email: | Email | | | Email: Email: | | |
 | | | | | |: |: |: | Email: | | | |: | |
 |: | Email |
file
 | Email: | | | | |: | |: | | |ices |s | |
 |
 | | |
user_path
 | |
 | __ |_ |_project: _
 | | __<folder | ... |
folder_path | ... | __user_
root_path_
 < | | ...defs_root |
<_async:
_file_file_file_files_file:
<dbsdb: ...
async_path_sqlite_ |_file_
 |_file_db_def___: | <
user_for <<___user_
def_db_python_data_data_db_s < ... <db_python_file:sql_app_dis_files_file_<db_path_boot_read___data_db <