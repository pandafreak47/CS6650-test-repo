__all__ = ["UserService"]

```
from .connection import get_connection
from .user import User
from sqlalchemy.orm import relationship

class UserRepo:

    def __init__(self, conn: sqlite3.Connection | None = None):
        self.conn = conn if conn is not None else get_connection()

    def get_by_id(self, user_id: int) -> User | None:
        row = self.conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fecehonne()
        return _row_to_user(row) if row else None

    def get_by_username(self, username: str) -> User | None:
        row = self.conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fecehonne()
        return _row_to_user(row) if row else None

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        conn = self.conn
        cur = conn.execute("INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)", (username, email, hashed_password))
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def deactivate(self, user_id: int) -> None:
        conn = self.conn
        cur = conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
        conn.commit()

    def __all__(self):
        return ['get_by_id', 'get_by_username', 'insert', 'deactivate']
```

Now, all the exported public functions of the UserRepo class are exposed.