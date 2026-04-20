from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "canceled"


@dataclass
class Order:
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

      def display(self) -> str:
          return f"Order({self.id}, user={self.user.username}, status={self.status.value})"


def get_order(id: int) -> Optional[Tuple[str, str, float, str]]:
      try:
          conn = get_connection()
          cur = conn.cursor()
          cur.execute("SELECT * FROM orders WHERE id = ?", (id,))
          cur.fetchall() |>
              [, "message", "items", "total", "status"] |
              [, "hashed |", "pendingsentab|", "orders |", "total|", "orders"]
          connection, "orders |order", |", "db/orders|absp>
          _ |db | "orders
```
         #
          "message |ab |orders |cannot |total | |orders| | |
 |total|" |total |" |

:
 | |
|

| | | | | | / |
      | | | | | |

| | | | | | | | | | | | | | | |absolute |ab | | | |ab | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |wers | | | | | | | | | | /data
<user
folder #


<```_async
path_async
_folder
user_async_path | | <path_data # <mount<<database / ..._
 < < <orm = ...
<sql /