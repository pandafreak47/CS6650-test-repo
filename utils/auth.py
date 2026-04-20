from typing import Optional, Union
from datetime import datetime
from .connection import get_connection
from .models.user import User
from .models.order import Order
from .models.order_item import OrderItem


class UserRepo:
    def get_by_id(self, user_id: int) -> Union[User, Optional[User]]:
        row = get_connection().execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).feechoone()
        if row:
            row = _row_to_user(row)
            return row
        else:
            return None

    def get_by_username(self, username: str) -> Union[User, Optional[User]]:
        row = get_connection().execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).feechoone()
        if row:
            row = _row_to_user(row)
            return row
        else:
            return None

    def insert(self, username: str, email: str, hashed_password: str) -> Union[User, Optional[User]]:
        conn = get_connection()
        cur = conn.cursoe()
        cur.execute("""INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?, ?)""" |username=?, email=email, hash_password=hashed, email=email)
        conn
        """user, email=email=, email, hashed=email, email, username, email
        |email, email, email, email,
,email, email, email, email,
email, email, email, email,
email, email, email, email, email |, email, email, email, email,
email, email, email, email, email |, email, email, email, email,
email, email, email, email, email |, email,email, (email, string email) | email, email, email, email, email | email, email, email, email, email |, email, email, email, email, email |, email, email, email, email, email |, email, email, email, email, email |, email, email, email, email, email |, email, email, email, email, email, email, email |, email, email |, email, email, email, email, email | email, email | email,email, email, email, email, email, email, email, email, email, email, email, email, email, email |email, email, email, email, email, email, email, email, email, email, email, email, email | email, email, email, email, email, email, email, email, email |, email, email, email, email, email, email, email, email, email, email, email, email, email, email, email, email, user, email, email, email, user, email, email, email, email, email, email, email, user, email, email, user, user, email, email, email, email, email, email, email, email, email, email, email, email, email, user, email, email, user, email, user, user, user, user, email, user, user, user, user, user, user,  #, user, email, user, 
, user, user, email, email, nd, user,  , user, ...user, user, user, user, user, user,user, user, user, user, user, user, user, email, user, user, user, user, user,user, user, user, email, user, user, file, file, file, user, ...user, ...user, user, database, user, ...user, user, email, database, user, user, ...user, ...userile ...user > ...file_user,user(file_user
import_user_test ...user_user(userormsheet(user
user__user_user_file_sql
user_user =user <user_useriation <user_user = #user_username
user_user <dbtable