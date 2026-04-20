from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pendinng"
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

# Rename the class name to match the task
class Order(OrderStatus, User, object):
       pass

# Use try-except block instead of bare excption
try:
     order = Order(1, User("username", "password"), ["item1", "item2"])
     try:
         order.status = OrderStatus.SHIPPED
         order.save()

     except Exception as e:
         print(f"Error while saving order: {e}")

     print(order.display())

except Exception as e:
     print(f"Error while saving order: {e}")
```