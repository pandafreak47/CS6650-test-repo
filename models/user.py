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

if __name__ == '__main__':
    pass