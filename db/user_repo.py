from .connection import get_connection
from .user import User

class UserRepo:
    
      def __init__(self, database_uri: str, username_col: str, password_col: str):
          self._username_col = username_col
          self._password_col = password_col
          self._database_uri = database_uri
          self._conn = None

      def get_by_id(self, user_id: int) -> User | None:
          row = get_connection().execute(
              f"SELECT * FROM users WHERE id = ?", (user_id,)
          ).fetchone()
          if row is not None:
              return _row_to_user(row)
          else:
              return None

      def get_by_username(self, username: str) -> User | None:
          row = get_connection().execute(
              f"SELECT * FROM users WHERE username = ?", (username,)
          ).fetchone()
          if row is not None:
              return _row_to_user(row)
          else:
              return None

      def insert(self, username: str, email: str, hashed_password: str) -> User:
          conn = get_connection()
          cur = conn.cursor()
          cur.execute("INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)", (username, email, hashed_password))
          conn.commit()
          return self.get_by_id(cur.lastrowid)

      def deactivate(self, user_id: int) -> None:
          conn = get_connection()
          cur = conn.cursor()
          cur.execute("UPDATE users SET is_active=? WHERE id=?", (1, user_id))
          conn.commit()

      def _row_0_username|username|email|hashed_password|email| |str|,
          ...
          email| |str| |self._username|email| |str|password| |str| |_username|email|
          | |username|email| |str| |_str| |user| |str|email|password| | |username |email| |password| | |str| |
 |email| |password| |str| |str |username| |str|
username| | | | | | | |username | | |str | | | | | | | | | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | /folder
self_path
 ... ...
 ...
_temp