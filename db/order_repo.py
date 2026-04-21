<task>
Add a new public API, adding the methods for getting all orders by user, creating a new order, updating an existing order, and deleting an order.
</task>
<file>
<file path="models/order.py">
from dataclasses import dataclass, field
from datetime import datetime


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