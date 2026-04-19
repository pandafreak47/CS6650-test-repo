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

    def __post_init__(self):
        """Validate input fields after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("id must be a positive integer")
        
        if not isinstance(self.username, str) or not self.username.strip():
            raise ValueError("username must be a non-empty string")
        
        if not isinstance(self.email, str) or not self.email.strip():
            raise ValueError("email must be a non-empty string")
        
        if "@" not in self.email or "." not in self.email.split("@")[1]:
            raise ValueError("email must be a valid email address")
        
        if not isinstance(self.hashed_password, str) or not self.hashed_password.strip():
            raise ValueError("hashed_password must be a non-empty string")
        
        if not isinstance(self.created_at, datetime):
            raise ValueError("created_at must be a datetime object")
        
        if not isinstance(self.is_active, bool):
            raise ValueError("is_active must be a boolean")

    def display(self) -> str:
        """Return a string representation of the user."""
        if not isinstance(self.username, str) or not isinstance(self.id, int):
            raise ValueError("Invalid user data for display")
        return f"User({self.id}, {self.username})"
```