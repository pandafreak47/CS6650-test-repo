```python
from db.user_repo import UserRepo
from models.user import User
from utils.validators import validate_email, validate_username
from utils.auth import hash_password

_repo = UserRepo()


class UserService:
    def register(self, username: str, email: str, password: str) -> User:
        username = validate_username(username)
        email = validate_email(email)
        
        if not isinstance(password, str):
            raise TypeError("password must be a string")
        password = password.strip()
        if not password:
            raise ValueError("password must not be blank")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        
        hashed = hash_password(password)
        return _repo.insert(username, email, hashed)

    def get(self, user_id: int) -> User:
        if not isinstance(user_id, int):
            raise TypeError("user_id must be an integer")
        if user_id <= 0:
            raise ValueError("user_id must be positive")
        
        user = _repo.get_by_id(user_id)
        if not user:
            raise LookupError(f"User {user_id} not found")
        return user

    def deactivate(self, user_id: int) -> None:
        if not isinstance(user_id, int):
            raise TypeError("user_id must be an integer")
        if user_id <= 0:
            raise ValueError("user_id must be positive")
        
        self.get(user_id)  # raises if not found
        _repo.deactivate(user_id)
```