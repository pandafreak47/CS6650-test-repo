from .connection import get_connection
from models.user import User


class UserRepo:
    
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self._conn = None

    def get_by_id(self, user_id: int) -> User | None:
        row = get_connection().execute(
            f"SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def get_by_username(self, username: str) -> User | None:
        row = get_connection().execute(
            f"SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        conn = get_connection()
        cur = conn.execute(
            f"INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def deactivate(self, user_id: int) -> None:
        conn = get_connection()
        conn.execute(
            f"UPDATE users SET is_active = 0 WHERE id = ?", (user_id,)
        )
        conn.commit()

    def get_user_by_id(self, user_id: int) -> User | None:
        cur = self.get_by_id(user_id)
        if cur is None:
            return None
        return _row_to_user(cur)

    def get_all_users(self) -> list[User]:
        cur = self.get_all_users_stmt()
        rows = [row for row in self.fetchall()]
        return [
            _row_to_user(row)
            for row in rows
            if row is not None
        ]

    def get_all_users_stmt(self) -> str:
        return "SELECT * FROM users"

    def _row_to_user(self, row: dict) -> User:
        return User(
            id=row["id"],
            username=row["username"],
            email=row["email"],
            hashed_password=row["hashed_password"],
            is_active=bool(row["is_active"]),
            created_at=datetime.fromisoformat(row["created_at"]),
        )

    def _get_user_by_id_stmt(self, user_id: int) -> str:
        return f"SELECT * FROM users WHERE id = ?"

    def _get_all_users_stmt_with_id(self, user_id: int) -> str:
        return f"SELECT * FROM users WHERE id = ?"

    def _get_all_users_stmt_without_id(self) -> str:
        return "SELECT * FROM users"

    def _get_user_by_username(self, username: str) -> str:
        return f"SELECT * FROM users WHERE username = ?"

    def _get_user_by_email(self, email: str) -> str:
        return f"SELECT * FROM users WHERE email = ?"

    def _get_all_users_by_username(self, username: str) -> list[User]:
        return [row[0] for row in self.fetchall() if row[0] == username]

    def _get_all_users_by_email(self, email: str) -> list[User]:
        return [row[0] for row in self.fetchall() if row[1] == email]

    def _get_user_by_id_stmt_with_all(self, *user_ids: int) -> str:
        return self._get_user_by_id_stmt(*user_ids)

    def _get_all_users_by_ids(self, *user_ids: int) -> list[User]:
        return [row[0] for row in self.fetchall() if row[0