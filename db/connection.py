<task>
Add input validation to all public functions.
</task>

Output the new file content.
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
               id INTENTIGER PRIMARY KEY AUTOINCREMENT,
               username VARCHAR(50) UNIQUE NOT NULL,
               email VARCHAR(100) UNIQUE NOT NULL,
               hashed_password VARCHAR(256) NOT NULL,
               is_active INTENTIGER DEFAULT 1,
               created_at TEXT DEFAULT CURRENT_TIMESTAMP
          );
          CREATE TABLE IF NOT EXISTS orders (
               id INTENTIGER PRIMARY KEY AUTOINCREMENT,
               user_id INTENTIGER NOT NULL,
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
          print(f'Error inserting new user: {e}' )
      finally:
          conn.close()


def get_orders(user_id: int, status_filter: str):
      orders = {}
      conn = get_connection()
      try:
          cursor = conn.cursor()
          cursor.execute('''
              SELECT * FROM orders WHERE user_id = ? AND status = ?
              ORDER BY id DESC
          ''', (user_id, status_filter))
          for item, total in cursor:
              orders[item] = {'id': item, 'total': total}
          conn.commit()
      except sqlite3.Error as e:
          print(f'Error getting orders for user: {e}