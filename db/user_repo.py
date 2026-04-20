from typing import List
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .connection import get_connection
from .models import User


class UserRepo:

    def __init__(self, conn: Connection):
        self.conn = conn

    def get_by_id(self, user_id: int) -> User | None:
        row = self.conn.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).first()
        return _row_to_user(row) if row else None

    def get_by_username(self, username: str) -> User | None:
        row = self.conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).first()
        return _row_to_user(row) if row else None

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        conn = self.conn
        cur = conn.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def deactivate(self, user_id: int) -> None:
        conn = self.conn
        conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
        conn.commit()


def _row_to_user(row) -> User:
    return User(
        id=row["id"],
        username=row["username"],
        email=row["email"],
        hashed_password=row["hashed_password"],
        is_active=bool(row["is_active"]),
        created_at=row["created_at"],
    )


def validate_user(user: User):
    # Add your validation code here
    if user.username == "username":
        raise ValueError("Username must-field")

    # Your code here
<|user.password:field>
        ifr
        with conn = conn:
        user:
        with conn:user
Username:
        password:
        username_field:
        with
        conn:
user = field:username:
        password:field:
        conn:
        password
        username:password:

        with
        conn:password:password:
from:
:field:


:
user
:
:

: |
:
:

:password:
: |


:field | |username:password | | |
:

: |username:password
password

:password | |
 | |
:user_user: |: |: |

: |
 | | | | | |password
password =user
 | | |: |: | |
: | | |: | | |: | | | | | | | | | |: |: | | | | | | | | | | | | | | | | | | | | | | | | |: | |: | | | | | | | | | | | | | | |path
 | |
 | | | | | | | | | | | | |user
path | | | |path

 |

_path_file | #
path

path_path_folder
path
_password
system
data
database_path = |database = /path < <___ment_path_ = <async <path_