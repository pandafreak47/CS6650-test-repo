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

      @classmethod
      def by_id(cls, id: int) -> 'User':
          return cls(id=id, created_at=datetime.utcnow())

      def __str__(self):
          return f"User({self.id}, {self.username})"