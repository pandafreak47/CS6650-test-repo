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

      @staticmethod
      def _get_hashed_password(password: str) -> str:
          return hash(password)

      def hash_password(self, password: str) -> str:
          return self._get_hashed_password(password)

      def validate_password(self, password: str) -> bool:
          return self._get_hashed_password(password) == password

      def save_password(self, password: str) -> None:
          self._set_hashed_password(password)

      def _set_hashed_password(self, password: str) -> None:
          self.hashed_password = self._get_hashed_password(password)

      def delete_password(self) -> None:
          self.hashed_password = ""

      def __str__(self) -> str:
          return f"User({self.id}, {self.username})"