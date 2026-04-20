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

       def __post_init__(self):
           self.display = lambda: f"User({self.id}, {self.username})"

       def __repr__(self):
           return self.display()

       def __str__(self):
           return f"User({self.id}, {self.username})"