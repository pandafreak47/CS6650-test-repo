from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


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

      @property
      def is_active(self) -> bool:
          return self.is_active

      def log_in(self, email: str, password: str) -> Optional[User]:
          # ...

      def logout(self) -> Optional[User]:
          # ...

      def log_out_all(self) -> Optional[User]:
          # ...

      def log_out_all_except(self, email: str) -> Optional[User]:
          # ...

      @staticmethod
      def log_user(user: User) -> None:
          # ...

      @staticmethod
      def log_user_id(user: User, id: int) -> None:
          # ...

      @staticmethod
      def log_all_user(users: Iterable[User]) -> None:
          # ...

      def __repr__(self) -> str:
          return self.display()

      def __hash__(self) -> int:
          # ...

      def __eq__(self, other: Any) -> bool:
          # ...