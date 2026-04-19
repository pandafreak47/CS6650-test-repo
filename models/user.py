from typing import Any, Dict, List, Optional
from dataclasses import dataclass
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

class UserWithToken(User):
     token: str = field(init=False)

class UserWithPassword(User):
     password: str = field(init=False)