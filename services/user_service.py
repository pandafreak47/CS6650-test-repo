```python
from db.user_repo import UserRepo
from models.user import User
from utils.validators import validate_email, validate_username
from utils.auth import hash_password

_repo = UserRepo()


class UserService:
    def register(self, username: str, email: str, password: str) -> User:
        """
        Register a new user with the provided credentials.
        
        Args:
            username: The desired username (3-32 alphanumeric/underscore characters).
            email: The user's email address.
            password: The user's password (minimum 8 characters).
        
        Returns:
            The newly created User object.
        
        Raises:
            ValueError: If username, email, or password validation fails.
        """
        validate_username(username)
        validate_email(email)
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        hashed = hash_password(password)
        return _repo.insert(username, email, hashed)

    def get(self, user_id: int) -> User:
        """
        Retrieve a user by their ID.
        
        Args:
            user_id: The ID of the user to retrieve.
        
        Returns:
            The User object with the specified ID.
        
        Raises:
            LookupError: If no user with the given ID exists.
        """
        user = _repo.get_by_id(user_id)
        if not user:
            raise LookupError(f"User {user_id} not found")
        return user

    def deactivate(self, user_id: int) -> None:
        """
        Deactivate a user account.
        
        Args:
            user_id: The ID of the user to deactivate.
        
        Raises:
            LookupError: If no user with the given ID exists.
        """
        self.get(user_id)  # raises if not found
        _repo.deactivate(user_id)
```