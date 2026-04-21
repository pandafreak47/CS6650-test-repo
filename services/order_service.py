<task>
Add a logging statement at the entry point of each public function.
</task>
<file path="db/order_repo.py">
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