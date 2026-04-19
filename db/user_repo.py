```python
from datetime import datetime
from .connection import get_connection
from models.user import User

# SQL Query Constants
_SQL_SELECT_ALL_BY_ID = "SELECT * FROM users WHERE id = ?"
_SQL_SELECT_ALL_BY_USERNAME = "SELECT * FROM users WHERE username = ?"
_SQL_INSERT_USER = "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)"
_SQL_UPDATE_DEACTIVATE = "UPDATE users SET is_active = 0 WHERE id = ?"

# Database Column Constants
_DB_COLUMN_ID = "id"
_DB_COLUMN_USERNAME = "username"
_DB_COLUMN_EMAIL = "email"
_DB_COLUMN_HASHED_PASSWORD = "hashed_password"
_DB_COLUMN_IS_ACTIVE = "is_active"
_DB_COLUMN_CREATED_AT = "created_at"

# Status Constants
_ACTIVE_STATUS_INACTIVE = 0

# Boolean Conversion Constants
_BOOL_TRUE = True


class UserRepo:
    def get_by_id(self, user_id: int) -> User | None:
        row = get_connection().execute(
            _SQL_SELECT_ALL_BY_ID, (user_id,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def get_by_username(self, username: str) -> User | None:
        row = get_connection().execute(
            _SQL_SELECT_ALL_BY_USERNAME, (username,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        conn = get_connection()
        cur = conn.execute(
            _SQL_INSERT_USER,
            (username, email, hashed_password),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def deactivate(self, user_id: int) -> None:
        conn = get_connection()
        conn.execute(_SQL_UPDATE_DEACTIVATE, (user_id,))
        conn.commit()


def _row_to_user(row) -> User:
    return User(
        id=row[_DB_COLUMN_ID],
        username=row[_DB_COLUMN_USERNAME],
        email=row[_DB_COLUMN_EMAIL],
        hashed_password=row[_DB_COLUMN_HASHED_PASSWORD],
        is_active=bool(row[_DB_COLUMN_IS_ACTIVE]),
        created_at=datetime.fromisoformat(row[_DB_COLUMN_CREATED_AT]),
    )
```