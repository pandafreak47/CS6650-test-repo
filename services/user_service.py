from db.user_repo import UserRepo
from models.user import User
from utils.validators import validate_email, validate_username
from utils.auth import hash_password

_repo = UserRepo()


class UserService:
    
    def register(self, username: str, email: str, password: str) -> User:
        validate_username(username)
        validate_email(email)
        
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        hashed = hash_password(password)
        return _repo.insert(username, email, hashed)

    
    def get(self, user_id: int) -> User:
        user = _repo.get_by_id(user_id)
        if not user:
            raise LookupError(f"User {user_id} not found")
        return user
    
    def deactivate(self, user_id: int) -> None:
        self.get(user_id)   # raise if not found
        _repo.deactivate(user_id)

```

In this example, we've added `LookupError` exception to the existing exception `ValueError`. This is because we need to raise this exception.

```python
raise LookupError("User does not exist")
```

In the code above, there are more than one file:

```python
```