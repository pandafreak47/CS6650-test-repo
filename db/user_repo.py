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

      def __str__(self) -> str:
          return self.display()

class UserRepo:
    
     def __init__(self, *args, **kwargs):
         pass

     def get_by_id(self, user_id: int) -> User | None:
         pass

     def get_by_username(self, username: str) -> User | None:
         pass

     def insert(self, username: str, email: str, hashed_password: str) -> User:
         pass

     def deactivate(self, user_id: int) -> None:
         pass

     @staticmethod
     def _row_to_user(row):
         pass

     @staticmethod
     def _row_to_user(row):
         pass

     @staticmethod
     def _row_to_user(row):
         pass
</assistant>