from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    id: int
    username: str
    email: str
    hashed_password: str

    def __hash__(self) -> int:
        return hash(self.username)

    def display(self) -> str:
        return f"User({self.id}, {self.username})"