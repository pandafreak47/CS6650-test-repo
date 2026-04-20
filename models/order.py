from typing import Optional, List, Union, Callable, Dict
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


@dataclass
class Order:
     id: int
     user: User
     items: List[str]
     total: float
     status: Union[OrderStatus, Callable[[str], OrderStatus]]
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

      def display(self) -> str:
         return f"Order({self.id}, user={self.user.username}, status={self.status.value})"