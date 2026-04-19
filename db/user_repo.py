from datetime import datetime
from .connection import get_connection
from .user_repo import UserRepo


class UserRepo:
    def __init__(self, db_path: str, conn: sqlite3.Connection | None = None) -> None:
        self.db_path = db_path
        self.conn = conn
        self.conn.row_factory = sqlite3.Row
        self.db = get_connection()

    def get_by_id(self, user_id: int) -> User | None:
        row = self.db.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        if row is None:
            return None
        return _row_to_user(row)

    def get_by_username(self, username: str) -> User | None:
        row = self.db.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        if row is None:
            return None
        return _row_to_user(row)

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        conn = self.conn
        cur = conn.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
        )
        conn.commit()
        return self.db.execute("SELECT * FROM users WHERE id = ?", (cur.lastrowid,)).fetchone()

    def deactivate(self, user_id: int) -> None:
        conn = self.conn
        conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
        conn.commit()

    def __all__(self):
        return ["get_by_id", "get_by_username", "insert", "deactivate"]


def _row_to_user(row) -> User:
    return User(
        id=row["id"], username=row["username"], email=row["email"],
        hashed_password=row["hashed_password"], is_active=bool(row["is_active"])
    )


class UserRepo(UserRepo):
    def __init__(self, db_path: str, conn: sqlite3.Connection | None = None) -> None:
        self.db_path = db_path
        self.conn = conn
        self.conn.row_factory = sqlite3.Row
        super().__init__(db_path, conn=self.conn)


if __name__ == "__main__":
    print(UserRepo().get_by_id(42))