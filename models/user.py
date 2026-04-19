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

     def display(self) -> str:
         return f"User({self.id}, {self.username})"

```

Output the file content, nothing else:
```
python models/user.py
User(id=1, username=username, email=email, hashed_password=hashed_password, created_at=datetime.datetime.now(), is_active=True)
```