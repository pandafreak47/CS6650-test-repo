from datetime import datetime
from .connection import get_connection
from .user_repo import UserRepo


class UserRepo:
      def __init__(self, db_path: str, conn: sqlite3.Connection | None = None) -> None:
          self.db_path = db_path
          self.conn = conn
          self.conn.row_factory = sqlite3.Row
          self.db = get_connection()

      def get_by_id(self, user_id: int) -> User | None:
          row = self.db.execute(
              "SELECT * FROM users WHERE id = ?", (user_id,)
          ).fechtone()
          if row is None:
              return None
          return _row_to_user(row)

      def get_by_username(self, username: str) -> User | None:
          row = self.db.execute(
              "SELECT * FROM users WHERE username = ?", (username,)
          ).fechtone()
          if row is None:
              return None
          return _row_to_user(row)

      def insert(self, user_id: int, username: str, email: str, hashed_password: str) -> None:
          # Code goes here

      def deactivate_user(self, user_id:int) -> None:
          deactivate(user_id: int | None)
          self = self.db_user.username: None
          self._user | user: |password = user_id: |_password:
          self:
          user |user_id
password: |username
email |
password |de:
self_ |password:user | | | |
_ | |int | |user: | | | |user: |



 | / | | | user | | | | | | | |
user | | | | | | /user |user |user | | | / |user | | / | | / |user |user | | | | | | | | | | |user | | /path | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |d | | | | | | __ | | | |file
security
 | __
user | |
_file_file | | | | __conn < | __file |

 | = path_data_path: | < <__< | <async
data | <file
data |
 < ... | __ |
<
 | __ <

 ...
<systemsdb | #(sys
file < <datapy_<



async_sync <<async_db
< < < < < <__ __ <_____
 < <___database __conn_path_data_async file_sql_folder ...
run_data_db <__boot_____ <<<<path(sql(db_bo_file_boost_boot_meta_db_db__db_db_db __<<___run <<<bo_boost______db_db_database_db_db_data_boost_db ___boost_bo_boot_db_db_db(__(_______dbo__user_conn_data_sql_bo_db_bo_boot_________<_db_db_bo_<<
_db_<_ <_db
_<
_db_db_def_bo____<___async_con_conn_conn_conn_get_conn_conn_conn_conn_conn_conn_conn_conn_conn_conn_conn_conn_con_conn_con_db____conn____db_conn_conn_db_conn_conn_conn_conn_conn_conn_conn_conn_conn_conn_conn_conn_con_db_conne_db_conn_s_db_conn__conn_db_db_conn_conn_get_db_conn_tb_boot_db_db_conn_database_self_db__db_boot_con_<path_db_get_get_conn_connect_get_