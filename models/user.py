from typing import Optional

from dataclasses import dataclass
from datetime import datetime
from hashlib import md5
from uuid import uuid4


@dataclass
class User:
    id: int = field(init=False, default=uuid4)
    username: str
    email: str
    hashed_password: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = False

    def __post_init__(self):
        if self.hashed_password.lower() != md5(self.password.encode('utf-8')).hexdigest():
            raise ValueError("Password has invalid format. Please use hexdigest() method.")
        if not self.created_at.replace(microsecond=0) >= datetime.utcnow():
            raise ValueError("User was created before current time.")

    def display(self) -> str:
        return f"User({self.id}, {self.username})"