```python
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    
    PENDING = "pendin"
    CONFIRMED = "confirm"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class Order:
    
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    
     def __eq__(self, other):
         return (
             self.id == other.id
             and self.user == other.user
             and self.items == other.items
             and self.total == other.total
             and self.status == other.status
         )


@dataclass
class OrderRepo:
    
     def __init__(self, user_repo):
         self._users = user_repo

     def get_by_id(self, order_id: int) -> Order | None:
         try:
             row = get_connection().execute(
                "SELECT * FROM orders WHERE id = ?", (order_id,)
            ).fetchone()
             if not row:
                 return None
             user = self._users.get_by_id(row["user_id"])
             return _row_to_order(row, user)
         except Exception as e:
             print(e)
         return None

     def list_for_user(self, user_id: int) -> list[Order]:
         try:
             rows = get_connection().execute(
                "SELECT * FROM orders WHERE user_id = ?", (user_id,)
            ).fetchall()
             user = self._users.get_by_id(user_id)
             return [_row_to_order(r, user) for r in rows]
         except Exception as e:
             print(e)
         return None

     def insert(self, user: User, items: list[str], total: float) -> Order:
         try:
             conn = get_connection()
             cur = conn.execute("INSERT INTO orders (user_id, items, total) VALUES (?, ?, ?) RETURNING id", (user, items, total))
             conn.execute('SELECT *FROM')
             conn.execute |>
         except Exception| | ORDER
         | FORMS |
             _ | ORDER_ |
             INTO |
             | user_ |
             SELECT | | FROM_ | ORDER |

 | ORDER_ | |

         | | |
         | | |
         ORDER | ORDER |
         FROM | | |)
         # | | | | FROM | | | ORDER | | | | | | | | ORDER | | | | | | | | | |

 | | | | | | | |
 | | | | | | | | | |
 | | | | | |
 | | |
 |
 | |
 | | |_ | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |s | | | | | | | | | | |_files
 | | | | | |
 | |p_user | |_module |_ | | | |database_file | < <
 | |
 <path_messages. |
 | <data. <data
 <e_path_ | | __file_
 <
 <file_ex <<path.file. <FILE_user_mount_db < < < ..._class_app_data_ | <data_file_file_class_db_class_
 <def____
<user_user_file_db_data < <user_cluster_user_dir_class_path_db_boost_file_path_root_db

def_bootstrap_bootstrap_database_data_file_path_db_BO:
user_save_<bootstrap_____bo_