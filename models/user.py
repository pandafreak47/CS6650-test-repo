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
        self._validate_id(self.id)
        self._validate_username(self.username)
        self._validate_email(self.email)
        self._validate_hashed_password(self.hashed_password)
        self._validate_created_at(self.created_at)
        self._validate_is_active(self.is_active)

    @staticmethod
    def _validate_id(id_value: int) -> None:
        """Validate id field."""
        if not isinstance(id_value, int) or id_value <= 0:
            raise ValueError("id must be a positive integer")

    @staticmethod
    def _validate_username(username: str) -> None:
        """Validate username field."""
        if not isinstance(username, str) or not username.strip():
            raise ValueError("username must be a non-empty string")

    @staticmethod
    def _validate_email(email: str) -> None:
        """Validate email field."""
        if not isinstance(email, str) or not email.strip():
            raise ValueError("email must be a non-empty string")
        
        if "@" not in email or "." not in email.split("@")[1]:
            raise ValueError("email must be a valid email address")

    @staticmethod
    def _validate_hashed_password(hashed_password: str) -> None:
        """Validate hashed_password field."""
        if not isinstance(hashed_password, str) or not hashed_password.strip():
            raise ValueError("hashed_password must be a non-empty string")

    @staticmethod
    def _validate_created_at(created_at: datetime) -> None:
        """Validate created_at field."""
        if not isinstance(created_at, datetime):
            raise ValueError("created_at must be a datetime object")

    @staticmethod
    def _validate_is_active(is_active: bool) -> None:
        """Validate is_active field."""
        if not isinstance(is_active, bool):
            raise ValueError("is_active must be a boolean")

    def display(self) -> str:
        """Return a string representation of the user."""
        if not isinstance(self.username, str):
            raise ValueError("username must be a string")
        if not isinstance(self.id, int):
            raise ValueError("id must be an integer")
        if self.id <= 0:
            raise ValueError("id must be a positive integer")
        return f"User({self.id}, {self.username})"
```