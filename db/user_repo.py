```python
from datetime import datetime
import sqlite3
from .connection import get_connection
from models.user import User


class UserRepo:
    def get_by_id(self, user_id: int) -> User | None:
        try:
            row = get_connection().execute(
                "SELECT * FROM users WHERE id = ?", (user_id,)
            ).fetchone()
            return _row_to_user(row) if row else None
        except sqlite3.DatabaseError:
            return None

    def get_by_username(self, username: str) -> User | None:
        try:
            row = get_connection().execute(
                "SELECT * FROM users WHERE username = ?", (username,)
            ).fetchone()
            return _row_to_user(row) if row else None
        except sqlite3.DatabaseError:
            return None

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        conn = get_connection()
        try:
            cur = conn.execute(
                "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
                (username, email, hashed_password),
            )
            conn.commit()
            return self.get_by_id(cur.lastrowid)
        except sqlite3.IntegrityError:
            conn.rollback()
            raise

    def deactivate(self, user_id: int) -> None:
        conn = get_connection()
        try:
            conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
            conn.commit()
        except sqlite3.DatabaseError:
            conn.rollback()
            raise


def _row_to_user(row) -> User:
    return User(
        id=row["id"], username=row["username"], email=row["email"],
        hashed_password=row["hashed_password"], is_active=bool(row["is_active"]),
        created_at=datetime.fromisoformat(row["created_at"]),
    )
```