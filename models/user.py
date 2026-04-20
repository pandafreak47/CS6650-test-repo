```python
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

     @property
     def display(self) -> str:
         return f"User({self.id}, {self.username})"

     @property
     def repr(self) -> str:
         return f"User(id={self.id}, username={self.username}, email={self.email}, password={self.hashed_password}, created_at={self.created_at}, is_active={self.is_active})"
```

```python
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

     @property
     def display(self) -> str:
         return f"User({self.id}, {self.username})"

     @property
     def repr(self) -> str:
         return f"User(id={self.id}, username={self.username}, email={self.email}, password={self.hashed_password}, created_at={self.created_at}, is_active={self.is_active})"
```

```python
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

     @property
     def display(self) -> str:
         return f"User({self.id}, {self.username})"

     @property
     def repr(self) -> str:
         return f"User(id={self.id}, username={self.username}, email={self.email}, password={self.hashed_password}, created_at={self.created_at}, is_active={self.is_active})"

class UserInput(validators.DataClassValidator):
     username: str
     email: str
     password: str

     @validator("username")
     def validate_username(self, values):
         if len(values["username"]) < 3:
             raise validators.ValidationError("Username must have at least 3 characters")
         return values

     @validator("email")
     def validate_email(self, values):
         try:
             email = emailaddress.validate(values["email"].lower())
             if not email or not emailaddress.valid(email):
                 raise validators.ValidationError(f"Invali<|system|> at least one of the given email address should be a valid email address")
             return values
         except emailaddress.emailaddresserror:
             raise validators.ValidationError(f"Invali<|user|> at least one of the given email address should be a valid email address: {values['email']}")

class UserValidator(dataclass):
     user_input: UserInput

     @classmethod
     def from_dict(cls, data: dict) -> 'UserValidator':
         return cls(UserInput.from_dict(data))

     @classmethod
     def from_json(cls, json_data: dict) -> 'UserValidator':
         return cls(UserInput.from_json(json_data))

     @classmethod
     def validate(cls, user_obj: User) -> None:
         validator = UserValidator()
         validator.validate(user_obj)

     @classmethod
     def __str__(cls):
         return cls.__repr__()

     @classmethod
     def __repr__(cls) -> str:
         return f"UserValidator(username={user_obj.username}, email={user_obj.email}, password={user_obj.password})"

     @classmethod
     def __rep__(cls):
         return f"UserValidator(username={user