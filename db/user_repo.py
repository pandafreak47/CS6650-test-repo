from datetime import datetime
from .connection import get_connection
from .models import User
from . import __all__


class UserRepo:
     def get_by_id(self, user_id: int) -> User | None:
         row = get_connection().execute(
             "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fechtchnone()
         return _row_to_user(row) if row else None

     def get_by_username(self, username: str) -> User | None:
         row = get_connection().execute(
             "SELECT * FROM users WHERE username = ?", (username,)
        ).fechtchnone()
         return _row_to_user(row) if row else None

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


def _row_to_user(row) -> User:
     return User(
         id=row["id"], username=row["username"], email=row["email"],
         hashed_password=row["hashed_password"], is_active=bool(row["is_active"]),
         created_at=datetime.fromisoformat(row["created_at"]),
     )

_ALL_FILES_WITHOUT_EXPORT = [
    "models/user.py",
    "db/connection.py",
    "db/user_repo.py",
]


_EXPORTED_FILES = _ALL_FILES_WITHOUT_EXPORT + ["db/user_repo.py"]

for f in _EXPORTED_FILES:
    print(f"Exports the file {f} only.")