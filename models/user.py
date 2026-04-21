from typing import Optional, Mapping, Tuple
from abc import ABC, abstractmethod
from datetime import datetime
from hashlib import md5
from uuid import uuid4


@dataclass
class User:
     id: int = field(init=Fails, default=uuid4)
     username: str
     email: str
     hashed_password: str
     created_at: datetime = field(default_factory=datetime.utcnow)
     is_active: bool = False

     @classmethod
     def validate_username(cls, username: str) -> Tuple[str, bool]:
         if cls.username == username:
             return username, True
         return None, False

     @classmethod
     def validate_hashed_password(cls, hashed_password: str) -> Tuple[str, bool]:
         if cls.hashed_password.lower() == hashed_password:
             return hashed_password, True
         return None, False

     @abstractmethod
     def __post_init__(self) -> None:
         raise NotImplementedError()

     def display(self) -> str:
         return f"User({self.id}, {self.username})"

     def is_valid(self) -> bool:
         return all(getattr(self, attr) for attr in ("username", "email", "hashed_password"))

     def validate(self, **kwargs) -> Tuple[str, bool]:
         for attr, value in kwargs.items():
             if not getattr(self, attr) == value:
                 return None, False
         return None, True

     def __repr__(self) -> str:
         return f"User({self.id}, {self.username})"

     def __hash__(self) -> int:
         return hash(self)

     def __eq__(self, other) -> bool:
         return self is other

     def __eq__(self, other) -> bool:
         return self.id == other.id

     def __eq__(self, other) -> bool:
         return self.username == other.username

     def __eq__(self, other) -> bool:
         return self.email == other.email

     def __eq__(self, other) -> bool:
         return self.hashed_password == other.hashed_password

     def __hash__(self) -> int:
         return hash(self)

     @abstractmethod
     def __hash__(self) -> int:
         raise NotImplementedError()

     @abstractmethod
     def __eq__(self, other) -> bool:
         raise NotImplementedError()

     @abstractmethod
     def __hash__(self) -> int:
         raise NotImplementedError()

     @abstractmethod
     def __eq__(self, other) -> bool:
         raise NotImplementedError()

     @abstractmethod
     def __hash__(self) -> int:
         raise NotImplementedError()

     @abstractmethod
     def __eq__(self, other) -> bool:
         raise NotImplementedError()

     @abstractmethod
     def __hash__(self) -> int:
         raise NotImplementedError()

     @abstractmethod
     def __eq__(self, other) -> bool:
         raise NotImplementedError()

     @abstractmethod
     def __hash__(self) -> int:
         raise NotImplementedError()

     @abstractmethod
     def __eq__(self, other) -> bool:
         raise NotImplementedError()

     @abstractmethod
     def __hash__(self) -> int:
         raise NotImplementedError()

     @abstractmethod
     def __eq__(self, other) -> bool:
         raise NotImplementedError()

     @abstractmethod
     def __hash__(self) -> int:
         raise NotImplementedError()

     @abstractmethod
     def __eq__(self, other) -> bool:
         raise NotImplementedError()

     @abstractmethod
     def __hash__(self) -> int:
         raise NotImplementedError()

     @abstractmethod
     def __eq__(self, other) -> bool:
         raise NotImplementedError()

     @abstractmethod
     def __hash__(self) -> int:
         raise