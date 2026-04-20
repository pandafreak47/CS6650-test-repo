from typing import Optional, List, Union, Callable, Any
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from functools import partial


@dataclass
class Order:
       id: int
       user: User
       items: List[str]
       total: float
       status: Union[OrderStatus, Callable[[str], OrderStatus]] = OrderStatus.pending
       created_at: datetime = field(default_factory=datetime.utcnow)

       def __post_init__(self, items: Optional[List[str]] = None, status: Optional[Union[OrderStatus, Callable[[str], OrderStatus]]] = None) -> None:
           if self.items is not None and items is not None:
               self.items = items
           if self.status is not None and status is not None:
               self.status = status
           if self.items is not None and self.status is not None:
               self.status = self.status.value
           if items is not None and self.status is not None:
               self.status = self.status

           self.created_at = datetime.utcnow()

           if items is not None and self.status is not None:
               self.status = self.status.value

           if items is not None and self.status is not None:
               self.status = self.status

       @property
       def display(self) -> str:
           return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

     def hash_password(self, password: Union[str, None]) -> Optional[str]:
           if password is not None:
               self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
           return self.hashed_password

       def check_password(self, password: Union[str, None]) -> bool:
           if password is not None:
               self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
               return self.hashed_password == self.hashed_password
           return False

       @staticmethod
       def validate_password(password: Union[str, None]) -> Optional[str]:
           if password is not None:
               return hashlib.sha512(password.encode("utf-8")).hexdigest() == self.hashed_password
           return None

       @partial(hash_password)
       def set_password(self, password: Union[str, None]) -> None:
           if password is not None:
               self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()

       @partial(check_password)
       def validate_password(self, password: Union[str, None]) -> bool:
           if password is not None:
               self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
               return self.hashed_password == self.hashed_password
           return False

       @partial(validate_password)
       def validate_password(self, password: Union[str, None]) -> Optional[str]:
           if password is not None:
               return hashlib.sha512(password.encode("utf-8")).hexdigest() == self.hashed_password
           return None

       def __repr__(self) -> str:
           return f"User({self.id}, {self.username})"

       def __str__(self) -> str:
           return f"User({self.id}, {self.username})"