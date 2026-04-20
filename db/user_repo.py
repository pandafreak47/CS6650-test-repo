from .connection import get_connection
from .user import User

class UserRepo:
    
    def __init__(self, database_uri: str, username_col: str, password_col: str):
        self._username_col = username_col
        self._password_col = password_col
        self._database_uri = database_uri
        self._conn = None

    def get_by_id(self, user_id: int) -> User | None:
        row = get_connection().execute(
            f"SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        if row is not None:
            return _row_to_user(row)
        else:
            return None

    def get_by_username(self, username: str) -> User | None:
        row = get_connection().execute(
            f"SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        if row is not None:
            return _row_to_user(row)
        else:
            return None

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def deactivate(self, user_id: int) -> None:
        conn = get_connection()
        conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
        conn.commit()

    def _row_to_user(self, row):
        return User(
            id=row[self._username_col],
            username=row[self._username_col],
            email=row[self._email_col],
            hashed_password=row[self._password_col],
            is_active=bool(row[self._isactive_col]),
            created_at=datetime.fromtimestamp(row[self._created_col]),
        )

```