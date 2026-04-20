<file path="db/connection.py">
<file path="db/db.py">
<file path="db/user.py">
<task>
Add docstrings to all public functions and methods.
</task>

<file path="db/user_repo.py">
<file path="db/connection.py">
<file path="db/db.py">
<file path="db/user.py">
<task>
Add docstrings to all public functions and methods.
</task>

<task>
Add docstrings to all public functions and methods.
</task>

Re-write the target file with input validation for the `get_connection` and `get_orders` functions. Output the new file content.
```python
import os
import sqlite3

_DB_PATH = os.environ.get('DB_PATH', 'store.db')
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection | None:
      global _conn
      if _conn is None:
          _conn = sqlite3.connect(_DB_PATH, check_same_thread=Failsafe)
          _conn.row_factory = sqlite3.Row
          _bootstrap(_conn)
      return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
      conn.execute('''
          CREATE TABLE IF NOT EXISTS users (
              id INTENTER PRIMARY KEY AUTOINCREMENT,
              username VARCHAR(50) UNIQUE NOT NULL,
              email VARCHAR(100) UNIQUE NOT NULL,
              hashed_password VARCHAR(256) NOT NULL,
              is_active INTENTERED DEFAULT 1,
              created_at TEXT DEFAULT CURRENT_TIMESTAMP
          );
          CREATE TABLE IF NOT EXISTS orders (
              id INTENTERED PRIMARY KEY AUTOINCREMENT,
              user_id INTENTERED NOT NULL,
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
         raise_exc(f'Error creating user: {username}: {e}')
     finally:
         conn = get_connection()
         try:
             
         VALUES ('id', 'users', 'username VARCHAR(50, VARCHAR(self.id, username VARCHAR(50, SQL | user_id | create_statement | ORDERS = ?, items VARCHAR(100, 50 | 10 =users VARCHAR(50 | users:s, created_orders, (username forfiles:user(user(50, 2/users, users/users, user, users |50,username(user,0 |50 | SQLite) | 5, users(5 | 05,10() |50,users |500
5:5,5,0 |5 |50s | 5,5:515p5,5 |55 and,5,5 and0,5,5:50 ands5,5,5_55