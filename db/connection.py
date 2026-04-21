<task>
Add input validation to all public functions.
</task>

Re-write the target file with input validation for the `get_connection` function. Output the new file content.
```python
import os
import sqlite3

_DB_PATH = os.environ.get('DB_PATH', 'store.db')
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection:
     global _conn
     if _conn is None:
         _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
         _conn.row_factory = sqlite3.Row
         _bootstrap(_conn)
     return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
     conn.execute('''
         CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username VARCHAR(50) UNIQUE NOT NULL,
             email VARCHAR(100) UNIQUE NOT NULL,
             hashed_password VARCHAR(256) NOT NULL,
             is_active INTEGER DEFAULT 1,
             created_at TEXT DEFAULT CURRENT_TIMESTAMP
         );
         CREATE TABLE IF NOT EXISTS orders (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             user_id INTEGER NOT NULL,
             items VARCHAR(100) NOT NULL,
             total REAL NOT NULL,
             status VARCHAR(20) DEFAULT 'pendin',
             created_at TEXT DEFAULT CURRENT_TIMESTAMP,
             FOREIGN KEY (user_id) REFERENCES users(id)
         );
     ''')
     conn.commit()


def get_user(user_id: int):
    return get_connection().execute('''
        SELECT * FROM users WHERE id = ?
    ''', (user_id,)).fetchone()


def create_user(username: str, email: str, password: str):
    conn = get_connection()
    try:
        create_statement = '''
            INSERT INTO users (username, email, hashed_password)
            VALUES (?, ?, ?)
        '''
        conn.execute(create_statement, (username, email, hashlib.sha256_finalize(password.encode('utf-8'))))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error inserting new user: {e}')
    finally:
        conn.close()


def get_orders(user_id: int) -> dict[int, dict[str, int]]:
    orders = {}
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT items, total
            FROM orders
            WHERE user_id = ?
        ''', (user_id,))
        for item, total in cursor:
            orders[item] = {'id': item, 'total': total}
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error getting orders for user: {e}')
    finally:
        conn.close()


def get_orders_by_id(order_id: int) -> dict[str, int]:
    orders = {}
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT items, total
            FROM orders
            WHERE id = ?
        ''', (order_id,))
        for item, total in cursor:
            orders[item] = total
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error getting orders for id: {e}')
    finally:
        conn.close()


def update_order(order_id: int, total_items: int, new_total_price: int):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE orders
            SET total = ?
            WHERE id = ?
        ''', (new_total_price, order_id))
        conn.commit()
    except sqlite3.Error as e:
        print(f'Error updating order: {e}')
    finally:
        conn.close()


def delete_order(order_id: int):
    conn