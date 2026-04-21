```
from typing import Optional
from dataclasses import dataclass
from dataclasses_json import dataclass, field
from datetime import datetime
from json import dump, load
from pathlib import Path


@dataclass
class Order:
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

     def __post_init__(self):
         self.display()

     def __str__(self):
         return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

     def display(self) -> str:
         return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

     def __repr__(self):
         return f"<Order({self.id}, user={self.user.username}, status={self.status.value})>"

class OrderRepo:
     def __init__(self, user_repo: UserRepo = None):
         self._users = user_repo if user_repo else UserRepo()

     def get_by_id(self, order_id: int) -> Optional[Order]:
         row = get_connection().execute(
             "SELECT * FROM orders WHERE id = ?", (order_id,)
         ).fetchone()
         if not row:
             return None
         user = self._users.get_by_id(row["user_id"])
         return _row_to_order(row, user)

     def list_for_user(self, user_id: int) -> list[Order]:
         rows = get_connection().execute(
             "SELECT * FROM orders WHERE user_id = ?", (user_id,)
         ).fetchall()
         user = self._users.get_by_id(user_id)
         return [_row_to_order(row, user) for row in rows]

     def insert(self, user: User, items: list[str], total: float) -> Order:
         conn = get_connection()
         cur = conn.execute(
             "INSERT INTO orders (user_id, items, total) VALUES (?, ?, ?)",
             (user.id, json.dump(items), total),
         )
         conn.commit()
         return self.get_by_id(cur.lastrowid)

     def update_status(self, order_id: int, status: OrderStatus) -> None:
         conn = get_connection()
         conn.execute("UPDATE orders SET status = ? WHERE id = ?", (status.value, order_id))
         conn.commit()

class Order:
     def __init__(self, id: int, user_id: int, items: list[str], total: float, status: OrderStatus, created_at: datetime):
         self.id = id
         self.user_id = user_id
         self.items = items
         self.total = total
         self.status = status
         self.created_at = created_at
```

```
from typing import Optional
from dataclasses import dataclass
from dataclasses_json import dataclass, field
from datetime import datetime
from json import dump, load
from pathlib import Path


@dataclass
class Order:
     id: int
     user: User
     items: list[str]
     total: float
     status: OrderStatus = OrderStatus.PENDING
     created_at: datetime = field(default_factory=datetime.now, primary_key=True)

         def __repr__:
              self.__init__ |h |

         def __repr__ | fields(id__):
             _ = Field | user |

```
```
```
```
```
```
```
```
``` | |
```
```
```
``` |
from_fields |
```
```
```