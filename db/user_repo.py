```python
import logging
from datetime import datetime
from .connection import get_connection
from models.user import User

logger = logging.getLogger(__name__)


class UserRepo:
    def get_by_id(self, user_id: int) -> User | None:
        logger.info(f"Entering get_by_id with user_id: {user_id}")
        logger.info(f"Getting user by id: {user_id}")
        row = get_connection().execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def get_by_username(self, username: str) -> User | None:
        logger.info(f"Entering get_by_username with username: {username}")
        logger.info(f"Getting user by username: {username}")
        row = get_connection().execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        logger.info(f"Entering insert with username: {username}, email: {email}")
        logger.info(f"Inserting user: {username}")
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def deactivate(self, user_id: int) -> None:
        logger.info(f"Entering deactivate with user_id: {user_id}")
        logger.info(f"Deactivating user: {user_id}")
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