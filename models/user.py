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

       def display(self) -> str:
           return f"User({self.id}, {self.username})"

class UserRegistration(User):
      password: str = field(default_factory=lambda: generate_password_hash(user.username))

def generate_password_hash(username: str) -> str:
   return bcrypt.generate_password_hash(username.encode('utf-8'), password_outside_the_cache=True)

def hash_password(password: str) -> str:
   return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12).encode('utf-8'))

if __name__ == '__main__':
   print(UserRegistration.display())
```

Now the `UserRegistration` class will be imported and the generated password hash will be printed at the end of the file, making it executable.

Note that in this example, the file `models/user.py` is exported only as a public API, so it should not be included in the source code of the package.