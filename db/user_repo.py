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