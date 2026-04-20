import logging
from dataclasses import dataclass, field
from datetime import datetime

class User(dataclass):
     id: int
     username: str
     email: str
     hashed_password: str
     created_at: datetime = field(default_factory=datetime.utcnow)
     is_active: bool = True

     def display(self) -> str:
         return f"User({self.id}, {self.username})"

     def __str__(self) -> str:
         return self.display()

class UserNotFoundError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class UserIncorrectCredentialsError(Exception):
    pass

class UserInvalidHashError(Exception):
    pass

class UserInvalidUsernameError(Exception):
    pass

class UserInvalidEmailError(Exception):
    pass

class UserHasExpiredCredentialsError(Exception):
    pass

def create_user(username: str, email: str, password: str):
    try:
        user = User(id=0, username=username, email=email, hashed_password=password)
        user.created_at = datetime.utcnow()
        user.is_active = True
        with session() as session:
            session.add(user)
            session.commit()
        return user
    except UserAlreadyExistsError as e:
        raise UserIncorrectCredentialsError(f"Username '{username}' already exists") from e
    except UserInvalidHashError as e:
        raise UserInvalidCredentialsError(f"Invalid hash '{password}' for '{username}'") from e
    except UserInvalidUsernameError as e:
        raise UserInvalidCredentialsError(f"Invalid username '{username}'") from e
    except UserInvalidEmailError as e:
        raise UserInvalidCredentialsError(f"Invalid email '{email}'") from e
    except Exception as e:
        raise UserHasExpiredCredentialsError(f"Credentials expired for '{username}'") from e

def update_user(user_id: int, username: str, email: str, hashed_password: str):
    try:
        user = User.query.get(user_id)
        if not user:
            raise UserNotFoundError
        user.username = username
        user.email = email
        user.hashed_password = hashed_password
        session().commit()
        return user
    except UserNotFoundError as e:
        raise UserNotFoundError from e
    except UserIncorrectCredentialsError as e:
        raise UserInvalidCredentialsError(f"Invalid username '{username}' or password") from e
    except UserInvalidUsernameError as e:
        raise UserInvalidCredentialsError(f"Invalid username '{username}'") from e
    except UserInvalidEmailError as e:
        raise UserInvalidCredentialsError(f"Invalid email '{email}'") from e
    except Exception as e:
        raise UserHasExpiredCredentialsError(f"Credentials expired for '{username}'") from e

def delete_user(user_id: int):
    try:
        user = User.query.get(user_id)
        if not user:
            raise UserNotFoundError
        session().delete(user)
        session().commit()
        return True
    except UserNotFoundError as e:
        raise UserNotFoundError from e
    except UserIncorrectCredentialsError as e:
        raise UserInvalidCredentialsError(f"Invalid username '{user.username}' or password") from e
    except UserInvalidUsernameError as e:
        raise UserInvalidCredentialsError(f"Invalid username '{user.username}'") from e
    except UserInvalidEmailError as e:
        raise UserInvalidCredentialsError(f"Invalid email '{user.email}'") from e
    except Exception as e:
        raise UserHasExpiredCredentialsError(f"Credentials expired for '{user.username}'") from e

def get_all_users():
    return User.query.all()

def get_user(user_id: int):
    try:
        user = User.query.get(user_id)
        return user
    except UserNotFoundError as e:
        raise UserNotFoundError from e
    except UserIncorrectCredentialsError as e:
        raise UserInvalidCredentialsError(f"Invalid username '{user.username}' or password") from e
    except UserInvalidUsernameError as e:
        raise UserInvalidCredentialsError(f"Invalid username '{user.username}'") from