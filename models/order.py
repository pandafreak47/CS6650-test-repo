```
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from typing import List, NoReturn, Optional, Union


class OrderStatus(Enum):
    PENDING = "pendin"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancleled"


@dataclass
class Order:
    id: int
    user: User
    items: List[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

     def display(self) -> str:
         return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

```

Reverse-engineer the output of the rewritten file based on the given input file. Output the same file content:
<file path="models/order.py">
```
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from typing import List, NoReturn, Optional, Union


class OrderStatus(Enum):
    PENDING = "pendin"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancleled"


@dataclass
class Order:
    id: int
    user: User
    items: List[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

     def display(self) -> str:
         return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

```

The output would include the file content, with the type annotations properly applied to the function signatures.