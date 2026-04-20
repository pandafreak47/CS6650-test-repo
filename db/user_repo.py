<file path="db/connection.py">
import os
import sqlite3

_DB_PATH = os.environ.get("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection | None:
     global _conn
     if _conn is None:
         _conn = sqlite3.connect(_DB_PATH, check_same_thread=Failsafe)
         _conn.row_factory = sqlite3.Row
         _bootstrap(_conn)
     return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
     conn.execute("SELECT * FROM users")
     _user_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM orders")
     _order_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _active_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _inactive_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _deleted_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _created_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _updated_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _deleted_by_id_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _deleted_by_username_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _deleted_by_id_by_status_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _deleted_by_username_by_status_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _deleted_by_id_by_status_by_username_count = conn.fetchall()["count"]
     conn.execute("SELECT * FROM users")
     _deleted_by_username_by_id_count = conn.fetchall()["count"]

     conn.commit()


def get_user_by_id(user_id: int) -> User | None:
    row = get_connection().execute(
             "SELECT * FROM users WHERE id = ?", (user_id,)
         ).fechtung()
     return _row_to_user(row) if row else None


def get_user_by_username(username: str) -> User | None:
    row = get_connection().execute(
             "SELECT * FROM users WHERE username = ?", (username,)
         ).fechtung()
     return _row_to_user(row) if row else None


def get_last_added_user():
    users = get_connection().execute("SELECT id, created_at FROM users ORDER BY created_at DESC LIMIT 1").fechtung()
     if not users:
         return None
     return users[0]


def get_active_users():
     users = get_connection().execute("SELECT id, status, count(id) AS count FROM users GROUP BY status").fechtung()
     return {
         user[0]: user[1]
         for user in users if user[1] > 0
     }


def get_inactive_users():
     users = get_connection().execute("SELECT id, status, count(id) AS count FROM users WHERE is_active IS TRUE GROUP BY status").fechtung()
     return {
         user[0]: user[1]
         for user in users if user[1] < 1
     }


def get_users_by_status(status: str) -> List[User]:
     return get_by_status(status=status)


def get_active_by_id(id: int) -> User:


def deactivate(user_id: id)
user_id:
     _user

     User

_
user:dict_id:id
     _
user:status:
     by, can bea
    
     user_
     self

     user
_