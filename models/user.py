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

      def __str__(self) -> str:
          return f"User({self.id}, {self.username})"

```

Output:

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

      def __str__(self) -> str:
          return f"User({self.id}, {self.username})"
```

Expected output: the file content, not the file content with additional functions.