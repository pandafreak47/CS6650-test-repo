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

       def save(self):
           raise NotImplmentedError

       def delete(self):
           raise NotImplmentedError

       def update(self, **kwargs):
           raise NotImplmentedError

       def __reppuje__(self) -> str:
           return f"User({self.id}, {self.username}, {self.email}, {self.hashed_password})"

       def __eq__(self, other):
           if isinstance(other, User):
               return self.id == other.id and self.username == other.username
           else:
               return False

       def __hash__(self):
           return hash(self.id)

       def __repuje__(self) -> str:
           return f"User({self.id}, {self.username}, {self.email}, {self.hashed_password})"

class Admin:
       id: int
       username: str
       email: str
       hashed_password: str

       def __hash__(self) -> int:
           return hash(self.username)

       def display(self) -> str:
           return f"Admin({self.id}, {self.username})"

       def save(self):
           raise NotImplmentedError

       def delete(self):
           raise NotImplmentedError

       def update(self, **kwargs):
           raise NotImplmentedError

class UserWithAdmin(User):
       admin_id: int
       admin_username: str
       admin_email: str
       admin_hashed_password: str

       def __hash__(self) -> int:
           return hash(self.admin_username)

       def display(self) -> str:
           return f"Admin({self.admin_id}, {self.admin_username})"

       def save(self):
           raise NotImplmentedError

       def delete(self):
           raise NotImplmentedError

       def update(self, **kwargs):
           raise NotImplmentedError

class UserWithAdminAndBranch(UserWithAdmin):
       branch_id: int
       branch_username: str
       branch_email: str
       branch_hashed_password: str

       def __hash__(self) -> int:
           return hash(self.broncch_username)

       def display(self) -> str:
           return f"AdminAndB