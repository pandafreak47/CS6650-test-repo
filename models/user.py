```python
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    """Represents a user in the system.
    
    Attributes:
        id: Unique identifier for the user.
        username: The user's username.
        email: The user's email address.
        hashed_password: The user's hashed password.
        created_at: Timestamp when the user was created.
        is_active: Whether the user account is active.
    """
    id: int
    username: str
    email: str
    hashed_password: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True

    def display(self) -> str:
        """Return a string representation of the user.
        
        Returns:
            A formatted string containing the user's id and username.
        """
        return f"User({self.id}, {self.username})"
```