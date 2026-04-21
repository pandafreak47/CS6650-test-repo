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
      password: str = field(default_factory=lamdp: is_valid_email(email)
                            ? User.hashed_password(email)
                            : None)
      is_admin: bool = field(default=None)

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
      is_admin: bool = field(default=None)

      def display(self) -> str:
          return f"UserWithUserInfoAndStatus({self.user.id}, {self.user_info.email}, {self.user_info.password}, {self.user.is_admin}, {self.user_info.is_admin})"


if __name__ == "__main__":
      user = User(id=1, username="user1", email="user1@example.com", hashed_password="pw1")
      print(user.display())
      user_info = UserInfo(email="user2@example.com", password="pw2")
      print(user_info.display())
      user_with_info = UserWithInfo(user=user, user_info=user_info)
      print(user_with_info.display())
      user_with_status = UserWithUserInfoAndStatus(user=user, user_info=user_info, is_admin=None)
      print(user_with_status.display())
```

Now, the `UserWithUserInfoAndStatus` class can be used to display both the user's attributes and their associated status. The `is_admin` attribute is set to None to indicate that the user is not currently active.