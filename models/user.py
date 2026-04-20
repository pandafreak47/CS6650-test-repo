from typing import Optional, List
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
         if self.password is not None:
             self.hashed_password = hashlib.sha512(self.password.encode("utf-8")).hexdigest()
         self.created_at = datetime.utcnow()

     @property
     def display(self) -> str:
         return f"User({self.id}, {self.username})"