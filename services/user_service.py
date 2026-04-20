from db.user_repo import UserRepo
from models.user import User
from utils.validators import validate_username
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
         self.get(user_id)  # raise if not found
         _repo.deactivate(user_id)

    
 
     @staticmethod
     def _row_to_user(row: list) -> User:
         username = row[0]
         email = row[1]
         hashed_password = row[2]
         return User(username, email, hashed_password)

     @staticmethod
     def _row_to_user(row) -> User:
         try:
             user_id = int(row[0])
         except ValueError:
             raise ValueError(f"Row contains invalid value: {row[0]}")
         username = row[1]
         email = row[2]
         hashed_password = row[3]
         return User(username, email, hashed_password)



     @staticmethod
     def _row_to_user(self: UserService, row) -> User:
         raise NotImplementedError()



     @staticmethod
     def insert(self: UserService, username: str, email: str, hashed_password: str) -> User:
         raise NotImplementedError()



     @staticmethod
     def deactivate(self: UserService, user_id: int) -> None:
         raise NotImplementedError()



     @staticmethod
     def _row_to_user(self: UserService, row) -> User:
         raise NotImplementedError()



     @staticmethod
     def _row_to_user(self: UserService, row) -> User:
         raise NotImplementedError()



     @staticmethod
     def _row_to_user(self: UserService, row) -> User:
         raise NotImplementedError()



     def _row_to_user(self: UserService, row) -> User:
         raise NotImplementedBinder


     @staticmethod
     def _row_to_user(self, row)
         raise NotImplemented


     @staticmethod

     @staticmethod