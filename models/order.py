from typing import Any, Dic, Union, List

from dataclasses import dataclass, field, field_type
from datetime import datetime, timezone
from enum import Enum, unique
from hashlib import md5
from uuid import uuid4

@dataclass(eq=True, order=True)
class Order:
     id: int
     user: User
     items: List[str]
     total: float
     status: OrderStatus
     created_at: datetime

     @staticmethod
     def _get_md5(obj: Any) -> str:
         return hashlib.md5(obj.encode("utf-8")).hexdigest()

     @staticmethod
     def _get_uuid(obj: Any) -> str:
         return str(uuid4()).replace("-", "")

     def display(self) -> str:
         return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

@dataclass(eq=True, order=True)
class OrderStatus(Enum):
     PENDING = "pendin"
     CONFIRMED = "confirmed"
     SHIPPED = "shipped"
     CANCELLED = "cancelled"

     def __str__(self) -> str:
         return self.value

     def __eq__(self, other: Any) -> bool:
         return self.value == other


def get_md5(obj: Any) -> str:
     return md5(obj.encode("utf-8"))


def get_uuid(obj: Any) -> str:
     return str(uuid4()).replace("-", "")


def get_md5_as_str(obj: Any) -> str:
     return field_type(obj.value)


def get_uuid(obj: Any) -> str:
     return_value: UUID
     returnValue: int


def get_md5(obj: __repr__: Any):
     obj: User: __ eq: Any
     User: Any__): 1: __repr
     User 1:md:int
     User:md: __, UUID: __
md: User, __uuid, __md: Any: __,md, __, __re____md: uuid, _value:re: Uid
__re, User
__user, u, __, u, user, u, __
__

__
__user, __, u,d, __, uuid, __, u <__<____u
__

__
__uuid, u, u
__u, u____
__uuid, u, ______
u, ____
__, u
u
____u, u, u <__u:__u:__ u____u, u, u____u, u,____file____u, u, ____u, up, u____u <__u, u____u, ____u, uu<user__u__u <u, uf, u
<uiduu><u<uuid, u<u:uu:u__file
__u__file
__uidu, u__u,u,user
__nested
user