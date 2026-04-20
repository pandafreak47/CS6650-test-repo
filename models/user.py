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
          self.is_active = True

      def display(self) -> str:
          return f"User({self.id}, {self.username})"