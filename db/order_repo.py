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


      def __all__:
          return ['Order']