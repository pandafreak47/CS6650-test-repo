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

    def __post_init__(self) -> None:
        """Validate all fields after initialization."""
        self._validate_id(self.id)
        self._validate_username(self.username)
        self._validate_email(self.email)
        self._validate_hashed_password(self.hashed_password)
        self._validate_created_at(self.created_at)
        self._validate_is_active(self.is_active)

    @staticmethod
    def _validate_id(value: int) -> None:
        """Validate id is a positive integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("id must be an integer")
        if value <= 0:
            raise ValueError("id must be a positive integer")

    @staticmethod
    def _validate_username(value: str) -> None:
        """Validate username is a non-empty string."""
        if not isinstance(value, str):
            raise TypeError("username must be a string")
        if not value or not value.strip():
            raise ValueError("username cannot be empty")
        if len(value) < 3:
            raise ValueError("username must be at least 3 characters long")
        if len(value) > 50:
            raise ValueError("username must not exceed 50 characters")

    @staticmethod
    def _validate_email(value: str) -> None:
        """Validate email is a non-empty string with valid format."""
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        if not value or not value.strip():
            raise ValueError("email cannot be empty")
        if "@" not in value or "." not in value:
            raise ValueError("email must be in a valid format")
        if len(value) > 255:
            raise ValueError("email must not exceed 255 characters")

    @staticmethod
    def _validate_hashed_password(value: str) -> None:
        """Validate hashed_password is a non-empty string."""
        if not isinstance(value, str):
            raise TypeError("hashed_password must be a string")
        if not value or not value.strip():
            raise ValueError("hashed_password cannot be empty")
        if len(value) < 20:
            raise ValueError("hashed_password must be at least 20 characters long")

    @staticmethod
    def _validate_created_at(value: datetime) -> None:
        """Validate created_at is a datetime object."""
        if not isinstance(value, datetime):
            raise TypeError("created_at must be a datetime object")

    @staticmethod
    def _validate_is_active(value: bool) -> None:
        """Validate is_active is a boolean."""
        if not isinstance(value, bool):
            raise TypeError("is_active must be a boolean")

    def display(self) -> str:
        """Return a string representation of the user."""
        if not isinstance(self.id, int) or not isinstance(self.username, str):
            raise ValueError("Invalid user data for display")
        return f"User({self.id}, {self.username})"
```