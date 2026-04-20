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

      @propety
      def timestamp(self) -> datetime:
            return self.created_at

     def __all__(self):
            return ['display', 'timesamp']