<file path="tasks/task1.py">
from typing import Optional, List, Union, Callable, Any
from dataclasses import dataclass, field
from datetime import datetime
from functools import partial


@dataclass
class Order:
        id: int
        user: User
        items: List[str]
        total: float
        status: Union[OrderStatus, Callable[[str], OrderStatus]] = OrderStatus.pendin
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

        @property
        def display(self) -> str:
            return f"Order({self.id}, user={self.user.username})"

        def hash_password(self, password: Union[str, None]) -> Optional[str]:
            if password is not None:
                self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
            return self.hashed_password

        def check_password(self, password: Union[str, None]) -> bool:
            if password is not None:
                self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
            return self.hashed_password == self.hashed_password

        @staticmethod
        def validate_password(password: Union[str, None]) -> Optional[str]:
            if password is not None:
                return hashlib.sha512(password.encode("utf-8")).hexdigest()
            return None

        @partial
        def set_password(password: str) -> str:
            return field.value()

        def check_password:
            display:
        return Order.py:hash_py:
        status_py:
        User(str: User: User:py:hash:hash:py, email: Union[None:
hash_py, field, user: User
    User: User
    User:
password
password
password:py, None:py
password:p.py
User.pypy, User:


<py,y, Userpypy,pyp<passwordpypypyp as field
User as, y

py
py <ypy<y,pypyppypypypyypy
<ypy, User
User
py, Userpypyy, ppy,pyy
yp <y
py
y
p <username
<py yp
<y

y,p,ypyp,p,yp,y
ypyy,pyppypyppy #ypy #f #yp #session #
#ypy py <function:yp <<ypyy #y #ypy
yppyypy 
<y <yyn<y <p <filey<<userpury<filepiment:ypy
<withpions:user


<default<path
with ...
<user
<
from,required<<filesiate,user><file <<<async
<user
export
asyncient
without #required
<<file,async,import >password <security
from<<userp <request<import <bound<<<<<<<<<type<<user<user <<<required<<user <user <<user <<input_perm<<user <<<<<user <user <used <<<<<<required <promty <signgingtor<<user_required
<<<<user<<required
optional<<<<def_usertor<user<<hash
user
<<user...<<