from datetime import datetime
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class User:
     id: int
     username: str
     email: str
     hashed_password: str
     created_at: datetime = field(default_factory=datetime.utcnow)
     is_active: bool = True

     def __repr__(self):
         return f"User({self.id}, {self.username}, {self.email})"

     def display(self):
         return f"User({self.id}, {self.username})"

     @classmethod
     def get_by_id(cls, user_id):
         row = cls.get(id=user_id)
         if not row:
             return None
         return cls(**row)

     @classmethod
     def get_by_username(self, username):
         row = self.get(username=username)
         if not row:
             return None
         return cls(**row)

     @classmethod
     def insert(cls, username, email, hashed_password):
         conn = cls.get_connection()
         cur = conn.execute(
             "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
             (username, email, hashed_password),
         )
         conn.commit()
         return cls.get_by_id(cur.lastrowid)

     @classmethod
     def deactivate(self, user_id):
         conn = self.get_connection()
         conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
         conn.commit()


def _row_to_user(row):
     return User(
         id=row['id'], username=row['username'], email=row['email'],
         hashed_password=row['hashed_password'], is_active=bool(row['is_active']),
         created_at=datetime.fromisoformat(row['created_at']),
     )

def get_user_by_username(username: str):
    return User.get_by_username(username)

def insert_user(username: str, email: str, hashed_password: str):
    return User.insert(username, email, hashed_password)

def deactivate_user(user_id: int):
    return User.deactivate(user_id)

def get_all_users():
    return User.get_all()

def get_user_by_id(user_id: int):
    return User.get_by_id(user_id)

def update_user_is_active(user_id: int, is_active: bool):
    return User.update(is_active=is_active, where_id=user_id)

def delete_user_by_id(user_id: int):
    return User.delete_by_id(user_id)

def get_all_user_by_is_active(is_active: bool):
    return User.get_by_is_active(is_active)

def get_all_user_by_username(username: str):
    return User.get_by_username(username)

def get_all_user_by_email(email: str):
    return User.get_by_email(email)

def get_all_user_by_username_and_email(username: str, email: str):
    return User.get_by_username_and_email(username, email)

def get_all_user_by_hashed_password(hashed_password: str):
    return User.get_by_hashed_password(hash_password=hash_password)

def get_all_user_by_username(username: str):
    return User(username=username)

get_orcid_password = User.get_or_id_or_password
 | username:username:username: |_
password:hashed | username:username:hash:
password:username:
    #:
username | password |username
password |username:_username |or_username: |username:password:username
:password |username:
:username |password: |username:


username:username: