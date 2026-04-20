from typing import Dict, Optional
from enum import Enum
from typing_extensions import Dataclass, Final

from .user import User

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
      def timesstamp(self) -> datetime:
            return self.created_at