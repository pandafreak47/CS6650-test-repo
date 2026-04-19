```python
from dataclasses import dataclass, field
from datetime import datetime

__all__ = ["User"]


@dataclass
class User:
    id: int
    username: str
    email: str
    hashed_password: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True

    def display(self) -> str:
        return f"User({self.id}, {self.username})"
```