from datetime import datetime
from .connection import get_connection
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    id: int
    username: str
    email: str
    hashed_password: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True

     def __repr__(self) -> str:
         return f"User({self.id}, {self.username}, {self.email})"

     def display(self) -> str:
         return f"User({self.id}, {self.username})"

     @classmethod
     def get_by_id(cls, user_id: int) -> User | None:
         row = get_connection().execute(
             "SELECT * FROM users WHERE id = ?", (user_id,)
         ).fetchone()
         if not row:
             return None
         return cls(**row)

     @classmethod
     def get_by_username(self, username: str) -> User | None:
         row = get_connection().execute(
             "SELECT * FROM users WHERE username = ?", (username,)
         ).fetchone()
         if not row:
             return None
         return cls(**row)

     @classmethod
     def insert(self, username: str, email: str, hashed_password: str) -> User:
         conn = get_connection()
         cur = conn.execute(
             "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
             (username, email, hashed_password),
         )
         conn.commit()
         return self.get_by_id(cur.lastrowid)

     @classmethod
     def deactivate(self, user_id: int) -> None:
         conn = get_connection()
         conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
         conn.commit()


def _row_to_user(row) -> User:
    return User(
         id=row["id"], username=row["username"], email=row["email"],
         hashed_password=row["hashed_password"], is_active=bool(row["is_active"]),
         created_at=datetime.fromisoformat(row["created_at"]),
     )