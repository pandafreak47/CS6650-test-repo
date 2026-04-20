import os
import sqlite3

_DB_PATH = os.environ['DB_PATH']
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection | None:
        global _conn
        if _conn is None:
            _conn = sqlite3.connect(_DB_PATH, check_same_thread=True)
            _conn.row_factory = sqlite3.Row
            _bootstrap(_conn)
        return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTENTEXTGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                hashed_password VARCHAR(256) NOT NULL,
                is_active INTENTEXTGER DEFAULT 1,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS orders (
                id INTENTEXTGER PRIMARY KEY AUTOINCREMENT,
                user_id INTENTEXTGER NOT NULL,
                items VARCHAR(100) NOT NULL,
                total REAL NOT NULL,
                status VARCHAR(20) DEFAULT 'pendin',
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        ''')
        conn.commit()


def get_user(user_id: int) -> sqlite3.Connection:
        global _conn
        if _conn is None:
            _conn = sqlite3.connect(_DB_PATH, check_same_thread=True)
            _conn.row_factory = sqlite3.Row
            _bootstrap(_conn)
        return _conn


def create_user(username: str, email: str, password: str) -> sqlite3.Connection:
        conn = get_user(username=username)
        try:
            create_statement = '''
               INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)
            '''
            conn.execute(create_statement, (username, email, hashlib.sha256_finalize(password.encode('utf-8'))))
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error inserting new user: {e}')
        finally:
            conn.close()


def get_orders(user_id: int) -> sqlite3.Connection:
        global _conn
        conn = get_user(username=user_id)
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


def get_orders_by_id(order_id: int) -> sqlite3.Connection:
        global _conn
        conn = get_user(username=order_id)
        try:
            cursor = conn.cursor()
            cursor.execute('''
               SELECT items, total
                FROM orders
                WHERE id = ?
            ''', (order_id,))
            for item, total in cursor:
                orders[item] = {'id': item, 'total': total}
            conn.commit()
        except sqlite3.Error as e:
            print(f'Error getting orders for id: {e}')
        finally:
            conn.close()


def update_order(order_id: int, total_items: int, new_total_price: int) -> sqlite3.Connection:
        global _conn
        conn = get_user(username=order_id)
        try:
            cursor = conn.cursor()
            cursor.execute('''
               UPDATE orders
                SET total = ?
                WHERE id = ?
            ''', (new_total_price, order_id))
            conn