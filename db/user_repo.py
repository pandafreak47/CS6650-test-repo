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

      def display(self) -> str:
          return f"User({self.id}, {self.username})"

```

Task:
Write an OOP Python program with a user registration feature that uses Django to handle user authentication. The program should include user authentication validation, user registration, and login authentication. The program should also include a user profile page displaying user details such as username, email, and password hash. The program should have a user sign-up form that prompts the user for their username, email, password, and confirms the password. The program should also validate the input and ensure that the username and email addresses are unique and that the password is valid. The program should also include user account management, including login verification and resetting passwords. The program should also include a feature that allows users to update their personal information and a feature that allows users to log out of their accounts.