from typing import TYPE_CHECKING

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

       @property
       def password(self) -> str:
           raise Exception("Password is not valid")

       def validate_password(self, password: str) -> bool:
           return password == self.password

       def __repr__(self) -> str:
           return f"User({self.id}, {self.username}, {self.email}, {self.hashed_password})"

if __name__ == '__main__':
       raise Exception("Invaliad file content")