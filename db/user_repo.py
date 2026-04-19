```python
from datetime import datetime
from .connection import get_connection
from models.user import User


class UserRepo:
    def get_by_id(self, user_id: int) -> User | None:
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer")
        
        row = get_connection().execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def get_by_username(self, username: str) -> User | None:
        if not isinstance(username, str) or not username.strip():
            raise ValueError("username must be a non-empty string")
        
        row = get_connection().execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        if not isinstance(username, str) or not username.strip():
            raise ValueError("username must be a non-empty string")
        if not isinstance(email, str) or not email.strip():
            raise ValueError("email must be a non-empty string")
        if not isinstance(hashed_password, str) or not hashed_password.strip():
            raise ValueError("hashed_password must be a non-empty string")
        
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def deactivate(self, user_id: int) -> None:
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("user_id must be a positive integer")
        
        conn = get_connection()
        conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
        conn.commit()


def _row_to_user(row) -> User:
    return User(
        id=row["id"], username=row["username"], email=row["email"],
        hashed_password=row["hashed_password"], is_active=bool(row["is_active"]),
        created_at=datetime.fromisoformat(row["created_at"]),
    )
```