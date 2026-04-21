from datetime import datetime
from .connection import get_connection
from models.user import User


class UserRepo:

    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def get_by_id(self, user_id: int) -> User | None:
        row = self.conn.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        if row is None:
            return None
        return _row_to_user(row)

    def get_by_username(self, username: str) -> User | None:
        row = self.conn.execute(
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
        return self.conn.execute("SELECT * FROM users WHERE id = ?", (cur.lastrowid,)).fetchone()[0]

    def deactivate(self, user_id: int) -> None:
        conn = self.conn
        cur = conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
        conn.commit()


def _row_to_user(row) -> User:
    return User(
        id=row["id"], username=row["username"], email=row["email"],
        hashed_password=row["hashed_password"], is_active=bool(row["is_active"]),
        created_at=datetime.fromisoformat(row["created_at"]),
    )


def get_user(user_id: int) -> User | None:
    conn = self.conn
    cur = conn.execute(
        "SELECT * FROM users WHERE id = ?", (user_id,)
    ).fetchone()
    if cur is None:
        return None
    return _row_to_user(cur)


def create_user(username: str, email: str, hashed_password: str) -> bool:
    conn = self.conn
    cur = conn.execute(
        "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
        (username, email, hashed_password),
    )
    conn.commit()
    return cur.rowcount == 1


def delete_user(user_id: int) -> bool:
    conn = self.conn
    cur = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    return cur.rowcount == 1


def get_all_users(cursor: sqlite3.Curso) -> list[User]:
    conn = self.conn
    query = "SELECT * FROM users"
    cursor.execute(query)
    results = conn.fetchall()
    return list(map(_row_to_user, results))


def get_by_username(username: str) -> User | None:
    conn = self.conn
    cur = conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()
    if cur is None:
        return None
    return _row_to_user(cur)


# noinspection PyUnboundLocalVariable:todo: retry
# noinspection SELint:unused
def _row_to_user(row: sqlite.Connection)

```