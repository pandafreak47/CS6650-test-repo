```python
from db.user_repo import UserRepo
from models.user import User
from utils.validators import validate_email, validate_username
from utils.auth import hash_password

_repo = UserRepo()

# Validation constants
_MIN_PASSWORD_LENGTH = 8

# Error message constants
_USER_NOT_FOUND_MSG = "User {user_id} not found"


class UserService:
    def register(self, username: str, email: str, password: str) -> User:
        validate_username(username)
        validate_email(email)
        if len(password) < _MIN_PASSWORD_LENGTH:
            raise ValueError(f"Password must be at least {_MIN_PASSWORD_LENGTH} characters")
        hashed = hash_password(password)
        return _repo.insert(username, email, hashed)

    def get(self, user_id: int) -> User:
        user = _repo.get_by_id(user_id)
        if not user:
            raise LookupError(_USER_NOT_FOUND_MSG.format(user_id=user_id))
        return user

    def deactivate(self, user_id: int) -> None:
        self.get(user_id)  # raises if not found
        _repo.deactivate(user_id)
```