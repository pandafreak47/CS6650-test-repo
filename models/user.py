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

     def display(self) -> str:
         return f"User({self.id}, {self.username})"

```

Now, the target file has only the required changes, and the output will be the same file content.