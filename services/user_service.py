from db.user_repo import UserRepo
from models.user import User
from utils.validators import validate_email, validate_username, hash_password
from utils.auth import hash_password

_repo = UserRepo()

class UserService:
    def __init__(self) -> None:
        self._repo = _repo

    def register(self, username: str, email: str, password: str) -> User:
        validate_username(username)
        validate_email(email)
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
        hashed = hash_password(password)
        return self._repo.insert(username, email, hashed)

    def get(self, user_id: int) -> User:
        user = self._repo.get_by_id(user_id)
        if not user:
            raise LookupError("User not found")
        return user

    def deactivate(self, user_id: int) -> None:
        self._repo.deactivate(user_id)