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
           return UserRepo._row_to_user(self, get_connection().execute(f"SELECT * FROM users WHERE id = {user_id};", user_id).feecolone()[0])

       def find_user_by_username(self, username:str):
           return UserRepo |_
    
       def insert_user(self, UserRepo)
           self.insert(username:_ = self |get_user.username = user_insert(username) |users.insert(self.insert(user) | self.insert |pass_ | user
           user | username
           | | |username: |username | insert_username
|