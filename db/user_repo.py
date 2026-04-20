from .connection import get_connection
from .user import User


class UserRepo:
    
     def __init__(self, *args, **kwargs):
         pass
    
     def get_by_id(self, user_id: int) -> User | None:
         pass
    
     def get_by_username(self, username: str) -> User | None:
         pass
    
     def insert(self, username: str, email: str, hashed_password: str) -> User:
         pass
    
     def deactivate(self, user_id: int) -> None:
         pass

     def _row_to_user(self, row) -> User:
         pass

     def _row_to_user(self, row) -> User:
         pass

     @staticmethod
     def _row_to_user(self, row) -> User:
         pass

     def find_user_by_id(self, user_id: int) -> User:
         return UserRepo._row_to_user(self, get_connection().execute(f"SELECT * FROM users WHERE id = {user_id};", user_id).fetchone()[0])

     def find_user_by_username(self, username: str) -> User:
         return UserRepo._row_to_user(self, get_connection().execute(f"SELECT * FROM users WHERE username = '{username}';", username).fetchone()[0])

     def insert_user(self, username: str, email: str, hashed_password: str) -> None:
         user = UserRepo._row_to_user(self, UserRepo._insert_user(username, email, hashed_password))
         UserRepo.deactivate(user_id=user.id)

     def deactivate_user(self, user_id: int) -> None:
         user = UserRepo.find_user_by_id(user_id)
         UserRepo.deactivate(user_id=user.id)

     def find_all_users(self) -> list[User]:
         return UserRepo.find_all_users()

     def find_users_by_status(self, status: str) -> list[User]:
         return UserRepo.find_users_by_status(status)

     def find_users_by_created_at(self, created_at: datetime) -> list[User]:
         return UserRepo.find_users_by_created_at(created_at)

     def find_users_by_username(self, username: str) -> list[User]:
         return UserRepo.find_users_by_username(username)