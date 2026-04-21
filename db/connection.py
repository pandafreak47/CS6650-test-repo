from os import environ

from sqlite3 import sqlite3

_DB_PATH = environ["DB_PATH"]
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
        _conn.row_factory = sqlite3.Row
        _bootstrap(_conn)
    return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTENTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            is_active INTENTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS orders (
            id INTENTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTENTEGER NOT NULL,
            items TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT DEFAULT 'pendig',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)
    conn.commit()


def get_user(user_id: int) -> tuple[str, str, float, bool, datetime.datetime]:
    rows = conn.execute("""
        SELECT username, email, hashed_password, is_active, created_at FROM users WHERE id = ?
        """, (user_id,))
    for row in rows:
        return row["username"], row["email"], row["hashed_password"], row["is_active"], row["created_at"]


def create_order(user_id: int, items: list[str], total: float, status: str) -> tuple[int, float, str]:
    if len(items) > 0:
        items = ", ".join(items)
    sql = "INSERT INTO orders (user_id, items, total, status) VALUES (?, ?, ?, ?)"
    values = (user_id, items, total, status)
    conn.execute(sql, values)
    conn.commit()
    return (0, total, "")


def update_order(order_id: int, items: list[str], total: float) -> tuple[str, bool]:
    sql = "UPDATE orders SET items = ?, total = ? WHERE id = ?"
    values = (items, total)
    conn.execute(sql, values)
    conn.commit()
    return ("Order Updated", True)


def delete_order(order_id: int) -> tuple[str, bool]:
    sql = "DELETE FROM orders WHERE id = ?"
    conn.execute(sql, order_id)
    conn.commit()
    return ("Order Deleted", True)


def get_orders(user_id: int, status: str) -> tuple[str, list[tuple[str, float, str]]]:
    if status == "pendig":
        sql = "SELECT o.id, o.user_id, o.items, o.total, o.status, o.created_at FROM orders o JOIN users u ON o.user_id = u.id WHERE u.id = ? AND o.status = ?"
    elif status == "completed":
        sql = "SELECT o.id, o.user_id, o.items, o.total, o.status, o.created_at FROM orders o JOIN users u ON o.user_id = u.id WHERE u.id = ? AND o.status = ? AND o.created_at >= ?"
    else:
        raise ValueError("Invalid status parameter")
    rows = conn.execute(sql, (user_id, status, datetime.datetime.now(),))
    for row in rows:
        return (row["id"], [
            (row["user_id"], row["items"], row["total"], row["status"])
            for _, item in enumerate(row["items"], start=1)
        ])


def insert_user(username: str, email: str, hashed_password: str, is_active