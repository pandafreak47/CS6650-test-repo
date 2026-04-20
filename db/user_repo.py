```python
from datetime import datetime
from dataclasses import dataclass, field
from data import User


@dataclass
class User:
    id: int
    username: str
    email: str
    hashed_password: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True

    def __post_init__(self):
        if self.password is not None:
            self.hashed_password = hashlib.sha512(self.password.encode("utf-8")).hexdigest()
        self.created_at = datetime.utcnow()

    @property
    def display(self):
        return f"User({self.id}, {self.username})"


class UserRepo:
    def get_by_id(self, user_id: int) -> User | None:
        row = self.get_connection().execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def get_by_username(self, username: str) -> User | None:
        row = self.get_connection().execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        return _row_to_user(row) if row else None

    def insert(self, username: str, email: str, hashed_password: str) -> User:
        conn = self.get_connection()
        cur = conn.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
        )
        conn.commit()
        return self.get_by_id(cur.lastrowid)

    def deactivate(self, user_id: int) -> None:
        conn = self.get_connection()
        conn.execute("UPDATE users SET is_active = 0 WHERE id = ?", (user_id,))
        conn.commit()


def _row_to_user(row) -> User:
    return User(
        id=row["id"],
        username=row["username"],
        email=row["email"],
        hashed_password=row["hashed_password"],
        is_active=bool(row["is_active"]),
        created_at=row["created_at"],
    )

```
</task>

Add a new input validation method to the file with the following code:

```python
def _validate_password(password: str) -> None:
    """Validates the given password.

    Args:
        password (str): The password to validate.

    Raises:
        ValueError: If the password is empty or does not contain at least one uppercase character.
        ValueError: If the password contains more than 128 characters.
    """
    if password and len(password) > 128:
        raise ValueError("Password should contain at least 128 characters")
    else:
        raise TypeError("Password shoulderservice")


# def get_password:str()
# Validates theraw password
def validate(password: str) -> List[User]
iface:
    """Allerservice:
    if password:
    """

while
```

This
def
"""
user:password:

"""user:
```

fromormage
from User
import
fromstring

<
fromuser, import
from
from,

<password

```
from <String>
from
from import
import
fromuser
```
fromuser
frompath


import
import
```
from
<import
from


user
import
user
<user
user>

user
<user
and a<user
user

user
connection
user,


user<user

user
user
user
user,user
user
<user
user,
user
user
<database
user
<user
<user
user
user
user
user

user
file
user,user


user
<user
user
user