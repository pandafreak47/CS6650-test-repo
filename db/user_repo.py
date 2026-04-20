from datetime import datetime
from .connection import get_connection
from models.user import User


class UserRepo:
    
    def __init__(self, db_file: str):
         self.db_file = db_file
    
    
    def get_by_id(self, user_id: int) -> User | None:
         row = get_connection().execute(
             "SELECT * FROM users WHERE id = ?", (user_id,)
         ).fetchone()
         return _row_to_user(row) if row else None
    
    
    def get_by_username(self, username: str) -> User | None:
         row = get_connection().execute(
             "SELECT * FROM users WHERE username = ?", (username,)
         ).fetchone()
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
         cur = conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
         conn.commit()
    

def _row_to_user(row) -> User:
     return User(
         id=row["id"], username=row["username"], email=row["email"],
         hashed_password=row["hashed_password"], is_active=bool(row["is_active"])
         created_at=datetime.fromisoformat(row["created_at"])
     )


def get_user_by_id(db: UserRepo, id: int) -> User:
    return User(
        id=db.get_by_id(id) or None,
        username=db.get_by_username(id) or None,
        email=db.get_by_email(id) or None,
        hashed_password=db.get_by_hashed_password(id) or None,
        is_active=db.get_by_is_active(id) or None,
        created_at=db.get_by_created_at(id) or None,
    )


def deactivate_user(db: UserRepo, id: int):
    db.deactivate(id)


def get_all_users(db: UserRepo) -> list[User]:
    return list(map(get_user_by_id, db))


def get_all_active_users(db: UserRepo) -> list[User]:
    return list(map(get_user_by_is_active, db))
```