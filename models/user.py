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
         raise NotImplementedError

     def delete(self):
         raise NotImplementedError

     def update(self, **kwargs):
         raise NotImplementedError

     def __repr__(self) -> str:
         return f"User({self.id}, {self.username}, {self.email}, {self.hashed_password})"

     def __eq__(self, other):
         if isinstance(other, User):
             return self.id == other.id and self.username == other.username
         else:
             return False

     def __hash__(self):
         return hash(self.id)

     def __repr__(self) -> str:
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
         raise NotImplementedError

     def delete(self):
         raise NotImplementedError

     def update(self, **kwargs):
         raise NotImplementedError

class UserWithAdmin(User):
     admin_id: int
     admin_username: str
     admin_email: str
     admin_hashed_password: str

     def __hash__(self) -> int:
         return hash(self.admin_username)

     def display(self) -> str:
         return f"UserWithAdmin({self.admin_id}, {self.admin_username}, {self.admin_email}, {self.admin_hashed_password})"

     def save(self):
         raise NotImplementedError

     def delete(self):
         raise NotImplementedError

     def update(self, **kwargs):
         raise NotImplementedError

class UserWithAdminAndBranch(UserWithAdmin):
     branch_id: int
     branch_username: str
     branch_email: str
     branch_hashed_password: str

     def __hash__(self) -> int:
         return hash(self.branch_username)

     def display(self) -> str:
         return f"UserWithAdminAndBranch({self.branch_id}, {self.branch_username}, {self.branch_email}, {self.branch_hashed_password})"

     def save(self):
         raise NotImplementedError

     def delete(self):
         raise NotImplementedError

     def update(self, **kwargs):
         raise NotImplementedError

class UserWithAdminAndBranchAndUser(UserWithAdminAndBranch):
     user_id: int
     user_username: str
     user_email: str
     user_hashed_password: str

     def __hash__(self) -> int:
         return hash(self.user_username)

     def display(self) -> str:
         return f"UserWithAdminAndBranchAndUser({self.user_id}, {self.user_username}, {self.user_email}, {self.user_hashed_password})"

     def save(self):
         raise NotImplementedError

     def delete(self):
         raise NotImplementedError

     def update(self, **kwargs):
         raise NotImplementedError

class UserWithAdminAndBranchAndUserAndRole(UserWithAdminAndBranchAndUser):
     role_id: int
     role_name: str

     def __hash__(self) -> int:
         return hash(self.role_name)

     def display(self) -> str:
         return f"UserWithAdminAndB