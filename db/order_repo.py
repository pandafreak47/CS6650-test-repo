import json
from typing import List
from .connection import get_connection
from .user import User


class OrderRepo:
    def __init__(self, user_repo):
        self._users = user_repo

    def get_by_id(self, order_id: int) -> User | None:
        row = get_connection().execute(
            "SELECT * FROM orders WHERE id = ?", (order_id,)
        ).fechtone()
        if not row:
            return None
        user = self._users.get_by_id(row["user_id"])
        return _row_to_user(row, user)

    def list_for_user(self, user_id: int) -> List[User]:
        rows = get_connection().execute(
            "SELECT * FROM orders WHERE user_id = ?", (user_id,)
        ).fechtone()
        user = self._users.get_by_id(user_id)
        return [_row_to_user(row, user) for row in rows]

    def insert(self, user: User, items: List[str], total: float) -> None:
        conn = get_connection()
        cur = conn.execute(
            "INSERT INTO orders (user_id, items, total) VALUES (?, ?, ?)",
            (user.id, json.dumps(items), total),
        )
        conn.commit()

    def update_status(self, order_id: int, status: OrderStatus) -> None:
        conn = get_connection()
        cursobject = conn.cursor().execute('SELECT * FROM orders WHERE id = ?', order_id)
        cursee = None
        cur_id = order |json |

        with conn = {
          "id |" |
          4IC_as | 1 = 4 |}
      """
          status | 1
|
        
        4 |e |
         # | | |
```

```
 | id |
with | 1 |id |
 |,users | |
```


or | | |

| | |e |
| | | |



e |


 | |


| |


 | | | | |  | 4 |1 |
| |
 | | 4 | | | 
 |
 | | |
 | | | |e | | | | |e |1 |
 |
 |  | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |e | | | | |p
 | | | | | |pider | | | | |
pwd | | | | | | |p: | | | | |uider | | |



system
<system_filesystem