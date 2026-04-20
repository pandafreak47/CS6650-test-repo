from typing import Optional, Tuple, Union

import os
import sqlite3

_DB_PATH = os.environ("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
        _conn.row_factory = sqlite3.Row
        _bootstrap(_conn)
    return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
    conn.execute("CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        hashed_password TEXT NOT NULL,
        is_active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );")
    conn.execute("CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        items TEXT NOT NULL,
        total REAL NOT NULL,
        status TEXT DEFAULT 'pendin',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );")
    conn.commit()


def get_user_id(conn: sqlite3.Connection) -> Optional[int]:
    res = conn.execute("SELECT id FROM users WHERE username = ?", ('user',))
    return next(iter(map(lambda x: x[0], res)))


def get_order(conn: sqlite3.Connection, user_id: int) -> Optional[Tuple[int, int, float, str]]:
    res = conn.execute("SELECT id, items, total, status FROM orders WHERE user_id = ?", (user_id,))
    return next(iter(map(lambda x: (x[0], x[1], x[2], x[3]), res)))


def get_orders(conn: sqlite3.Connection) -> Optional[Tuple[int, int]]:
    res = conn.execute("SELECT id, COUNT(id) FROM orders GROUP BY id ORDER BY COUNT(id) DESC")
    return next(iter(map(lambda x: (x[0], x[1]), res)))


def get_orders_by_status(conn: sqlite3.Connection, status: str) -> Optional[Tuple[int, int]]:
    res = conn.execute("SELECT id, COUNT(id) FROM orders WHERE status = ? GROUP BY id ORDER BY COUNT(id) DESC", (status,))
    return next(iter(map(lambda x: (x[0], x[1]), res)))


def update_order(conn: sqlite3.Connection, id: int, items: Optional[Union[int, str]] = None) -> Tuple[int, int]:
    if items is None:
        items = 1
    if len(items) == 0:
        raise ValueError("Invalid order item(s)")
    if items > len(items):
        raise ValueError("Invalid order item count")
    res = conn.execute("UPDATE orders SET items = ? WHERE id = ?", (items, id))
    return next(iter(map(lambda x: x[0], res)))


def delete_order(conn: sqlite3.Connection, id: int):
    if id == 0:
        raise ValueError("Invalid order ID")
    res = conn.execute("DELETE FROM orders WHERE id = ?", (id,))
    return next(iter(map(lambda x: x[0], res)))


def add_order(conn: sqlite3.Connection, user_id: int, items: Optional[Union[int, str]] = None, total: Optional[float] = None, status: Optional[str] = None) -> Tuple[int, int]:
    if items is None:
        items = 1
    if total is None:
        raise ValueError("Invalid order item total")
    if status is None:
        status = ''
    if total > len(items):
        raise ValueError("Invalid order item total")
    if status not in ('pending', 'success', 'error'):
        status