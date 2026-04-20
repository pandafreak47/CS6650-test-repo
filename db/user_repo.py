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
         id=row["id"], username=row["username"], email=row["email"],
         hashed_password=row["hashed_password"], is_active=bool(row["is_active"]),
         created_at=row["created_at"],
     )