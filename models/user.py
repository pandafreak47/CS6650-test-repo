```python
from dataclasses import dataclass, field
from datetime import datetime

# Default values
DEFAULT_ACTIVE_STATUS = True

# Display format
USER_DISPLAY_FORMAT = "User({}, {})"


@dataclass
class User:
    id: int
    username: str
    email: str
    hashed_password: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = DEFAULT_ACTIVE_STATUS

    def display(self) -> str:
        return USER_DISPLAY_FORMAT.format(self.id, self.username)
```