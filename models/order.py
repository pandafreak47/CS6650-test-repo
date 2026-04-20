from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


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

```

Explanation:

1. Define the `OrderStatus` enum type in the `user` class:

   - `PENDING` represents an order that is being processed by the user.
   - `CONFIRMED` represents an order that has been confirmed by the user.
   - `SHIPPED` represents an order that has been shipped by the user.
   - `CANCELLED` represents an order that was cancelled by the user.

   These enum values are used in the `Order` class's `status` attribute.

2. Add type annotations to all function signature in the `models` module.

   ```python
   from dataclasses import dataclass, field
   from datetime import datetime

   @dataclass
   class User:
       id: int
       username: str
       email: str
       hashed_password: str
       created_at: datetime = field(default_factory=datetime.utcnow)
       is_active: bool = True

   @dataclass
   class Order:
       id: int
       user: User
       items: list[str]
       total: float
       status: OrderStatus = OrderStatus.PENDING
       created_at: datetime = field(default_factory=datetime.utcnow)
   ```

   This approach ensures that all function signatures are fully type-annotated, making it easier to debug and understand any errors that might arise.

3. Add type annotations to the `models/order.py` file, including the `Order` class.

   ```python
   from dataclasses import dataclass, field
   from datetime import datetime
   from enum import Enum
   from .user import User

   class OrderStatus(Enum):
       PENDING = "pendin..."
       CONFIRMED = "confirmed..."
       SHIPPED = "shipped..."
       CANCELLED = "cancelled..."

   @dataclass
   class Order:
       id: int
       user: User
       items: list[str]
       total: float
       status: OrderStatus = OrderStatus.PENDING
       created_at: datetime = field(default_factory=datetime.utcnow)

   ```

   This file ensures that all `Order` class attributes and methods are fully type-annotated, making it easier to write and debug tests.