from datetime import datetime
from .connection import get_connection
from .user_repo import UserRepo


class UserRepo:
    
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
        conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
        conn.commit()


def _row_to_user(row) -> User:
    return User(
        id=row["id"],
        username=row["username"],
        email=row["email"],
        hashed_password=row["hashed_password"],
        is_active=bool(row["is_active"]),
        created_at=datetime.fromisoformat(row["created_at"]),
    )


def main():
    repo = UserRepo()

    # Insert a new user
    username = "JohnDoe"
    email = f"{username}.example.com"
    hashed_password = bcrypt.generate_password_hash(str(username).encode()).decode()
    repo.insert(username, email, hashed_password)

    # Deactivate a user
    user_id = 1
    repo.deactivate(user_id)

    # Get a user by ID
    user = repo.get_by_id(user_id)
    print(user)

    # Get a user by username
    user = repo.get_by_username("JohnDoe")
    print(user)

    # Get all users by status
    users = repo.get_by_status("active")
    for user in users:
        print(user)

    # Get the last added user
    users = repo.get_by_status("pending")
    print(f"Last added user: {users[-1]}")

    conn = get_connection()
    conn.close()


if __name__ == "__main__":
    main()

```