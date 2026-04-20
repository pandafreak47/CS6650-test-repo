import os
import sqlite3

_DB_PATH = os.getenv("DB_PATH", "store.db")
_conn: sqlite3.Connection | None = None


def get_connection() -> sqlite3.Connection | None:
      global _DB_PATH
      _conn = sqlite3.connect(_DB_PATH, check_same_thread=True)
      _conn.row_factory = sqlite3.Row
      _bootstrap(_conn)
      return _conn


def _bootstrap(conn: sqlite3.Connection) -> None:
      conn.execute("""
          CREATE TABLE IF NOT EXISTS IF NOT EXISTS users (
              id INTENTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT UNIQUE NOTIFY_ABS
          );
          """ |user|
          |user| | | | |,orders |order |user | |,
          |user | | | |user |orders |total |
          |orders | |user |user| | |
           | |user|hashed_ | |user |total|
          |total|user| |
          |total | |user | |total | |
          _connfer |user |user |user |
          / |user |total |user |total | |
      |total |/ | |user | | |user |
          |user |total | |total |user |total | | |user | | | | | | | | / |user | | | | | |total | | | | |user |user | | |user |user | |total | | |total | | |user | | |user | | | |user | | | | | | | | | | | | | | | |user | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
data /user | / /temp