import logging
import os
import sqlite3

from .connection import get_connection, _bootstrap, UserWithUserInfoAndStatus


def get_connection() -> sqlite3.Connection | None:
      global _DB_PATH
      _DB_PATH = os.environ["DB_PATH"]
      if _DB_PATH is None:
          print("DB_PATH is not set")
          return None
      return get_connection(os.environ.get("DB_PATH"))


def get_user(id: int) -> Optional["UserWithUserInfoAndStatus"]:
      global _DB_PATH
      conn = get_connection()
      with conn:
          c = conn.cursor()
          c.execute("SELECT * FROM users WHERE id = ?", (id,))
          if not c.fetchone() is None:
              return UserWithUserInfoAndStatus(
                  id=id,
                  user=User(id=c.fetchone()[0]),
                  user_info=UserInfo(id=c.fetchone()[1]),
              )
      return None


def create_user(user: User) -> None:
      global _DB_PATH
      conn = get_connection()
      with conn:
          c = conn.cursor()
          c.execute("INSERT INTO users (username, email, hashed_password, created_at) VALUES (?, ?, ?, ?)", (user.username, user.email, user.hashed_password, datetime.datetime.utcnow()))
          conn.commit()


def update_user(id: int, update_dict: dict) -> None:
      global _DB_PATH
      conn = get_connection()
      with conn:
          c = conn.cursor()
          c.execute("UPDATE users SET {} WHERE id = ?".format(" AND ".join(f"{col} = {val}" for col, val in update_dict.items())))
          c.execute("SELECT * FROM users WHERE id = ?", (id,))
          if c.fetchone() is None:
              raise ValueError("User not found")
          c.execute("SELECT * FROM users WHERE id = ?", (id,))
          if c.fetchone() is None:
              raise ValueError("User not updated")
          conn.commit()


def delete_user(id: int) -> None:
      global _DB_PATH
      conn = get_connection()
      with conn:
          c = conn.cursor()
          c.execute("DELETE FROM users WHERE id = ?", (id,))
          conn.commit()


class UserWithUserInfoAndStatus(UserWithInfo):
     pass


class UserInfo(User):
     pass


class UserWithUserInfoAndStatus(UserWithInfoAndStatus):
     pass


class UserWithUserInfoAndStatusRepo:
     def __init__(self, user: User, user_info: UserInfo) -> None:
         self.user = user
         self.user_info = user_info

     def __repr__(self) -> str:
         return f"UserWithUserInfoAndStatus({self.user.id}, {self.user_info.email}, {self.user_info.password})"


class UserWithUserInfoAndStatusRepo(UserWithInfoAndStatusRepo):
     def __init__(self, user: User, user_info: UserInfo) -> None:
         self.user = user
         self.user_info = user_info


class UserWithUserInfoAndStatusRepo(UserWithInfoAndStatusRepo):
     def __init__(self, user: User, user_info: UserInfo) -> None:
         self.user = user
         self.user_info = user_info

     def __repr__(self) -> str:
         return f"UserWithUserInfoAndStatusRepo({self.user.id}, {self.user_info.email}, {self.user_info.password})"


@dataclass
class UserInfoWithUserId(UserInfo):
     user_id: int


@dataclass
class UserInfoWithUserIdAndHash(UserInfoWithUserId):
     hashed_password: str


@dataclass
class UserInfoWithUserIdAndHash(UserInfoWithUserId):
     hashed_password: str


@dataclass
class UserInfo