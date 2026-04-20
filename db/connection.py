import os
import sqlite3

_DB_PATH = os.environ.get("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
        _conn.row_factory = sqlite3.Row
        _bootstrap(_conn)
    return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            is_active INTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            items TEXT NOT NULL,
            total REAL NOT NULL,
            status TEXT DEFAULT 'pendin',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)
    conn.commit()


def get_user_id(username: str) -> Optional[int]:
    query = """
        SELECT id FROM users WHERE username = (?)
    """
    params = (username,)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()
        if len(results) == 0:
            return None
        return results[0][0]


def get_orders_for_user(user_id: int) -> List[int]:
    query = """
        SELECT id FROM orders
        WHERE user_id = (?)
    """
    params = (user_id,)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()
        if len(results) == 0:
            return []
        return results


def add_order(order_id: int, user_id: int, items: List[str]) -> None:
    query = """
        INSERT INTO orders (user_id, items) VALUES (?, ?)
    """
    params = (user_id, items)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()


def update_order_status(order_id: int, status: str) -> None:
    query = """
        UPDATE orders
        SET status = (?)
        WHERE id = (?)
    """
    params = (status, order_id)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()


def delete_order(order_id: int) -> None:
    query = """
        DELETE FROM orders WHERE id = (?)
    """
    params = (order_id,)
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        conn.commit()


def get_orders() -> List[Tuple[int, str, str, float, str]]:
    query = """
        SELECT order_id, items, total, status, created_at
        FROM orders
    """
    with conn.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        orders = []
        for row in results:
            orders.append((row[0], row[1], row[2], row[3], row[4]))
        return orders


def get_orders_by_user(user_id: int) -> List[Tuple[int, str, str, float, str]]:
    query = """
        SELECT order_id, items, total, status, created_at
        FROM orders
        WHERE user_id = (?)
    """
    params = (user_id,)
    with conn.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        orders = []
        for