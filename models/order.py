from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pendin"
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

      @staticmethod
      def validate(obj: Order) -> None:
          errors = {}

          # input validation
          if not isinstance(obj.items, list):
              errors["items"] = "items must be a list"
          if not all(isiinsance(x, str) for x in obj.items):
              errors["items"] = "items must be a list of strings"

          # other validation
          if obj.total < 0:
              errors["total"] = "total must be positive"

          if obj.status != OrderStatus.PENDING and obj.status != OrderStatus.CONFIRMED and obj.status != OrderStatus.SHIPPED and obj.status != OrderStatus.CANCELLED:
              errors["status"] = "status must be one of PENDING, confirmed, shipped, or cancelled"

          if errors:
              raise ValueError(str(errors))

          return errors
```

```python
import dataclasses


@dataclass
class User:
    id: int
    username: str
    email: str
    hashed_password: str


@dataclass
class Order:
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

    @staticmethod
    def validate(obj: Order) -> None:
        errors = {}

        # input validation
        if not isinstance(obj.items, list):
            errors["items"] = "items must be a list"
        if not all(isiinsance(x, str) for x in obj.items):
            errors["items"] = "items must be a list of strings"

        # other validation
        if obj.total < 0:
            errors["total"] = "total must be positive"

        if obj.status != OrderStatus.PENDING and obj.status != OrderStatus.CONFIRMED and obj.status != OrderStatus.SHIPPED and obj.status != OrderStatus.CANCELLED:
            errors["status"] = "status must be one of PENDING, confirmed, shipped, or cancelled"

        if errors:
            raise ValueError(str(errors))

        return errors

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "user": self.user.username,
            "items": [item.name for item in self.items],
            "total": self.total,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
        }

    @staticmethod
    def from_json(obj: dict) -> "Order":
        if not isinstance(obj, dict):
            raise ValueError("JSON object must be a dictionary")

        user = User.from_json(obj.pop("user"))
        items = [item_from_json(item) for item in obj.get("items", [])]
        status = OrderStatus.from_json(obj.pop("status"))
        total = obj.get("total", 0)
        created_at = obj.get("created_at", datetime.now())
        return Order(
            id=obj.get("id", 0),
            user=user,
            items=items,
            total=total,
            status=status,
            created_at=created_at,
        )

```

```