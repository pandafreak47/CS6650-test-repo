from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field, field_type
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
          if self.username == "":
              raise ValueError("username cannot be empty")

      def display(self) -> str:
          return f"User({self.id}, {self.username})"

      @classmethod
      def from_tuple(cls, tup: Tuple[str, ...]) -> "User":
          return cls(username=tup[0], email=tup[1])

class UserWithToken(User):
      token: str = field(init=field_type(str))

class UserWithPassword(User):
      password: str = field(init=field_type(str))