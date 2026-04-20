from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
        id: int
        username: str
        email: str
        hashed_password: str
        created_at: datetime = field(default_factory=datetime.utcnow)
        is_active: bool = True

        def __post_init__(self):
            self.display = lambda: f"User({self.id}, {self.username})"

        def __repr__(self):
            return self.display()

        def __str__(self):
            return f"User({self.id}, {self.username})"

        def __repr__(self):
            return self.display()

        def __str__(self):
            return f"User({self.id}, {self.username})"

        def __hash__(self):
            return hash(self.id)

        def __eq__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return self.id == other.id

        def __lt__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return self.id < other.id

        def __le__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return self.id <= other.id

        def __gt__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return self.id > other.id

        def __ge__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return self.id >= other.id

        def __contains__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return self.id in other.id

        def __reversed__(self):
            return [other for other in self]

        def __add__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return User(self.id + other.id, self.username + other.username)

        def __sub__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return User(self.id - other.id, self.username - other.username)

        def __mul__(self, other):
            if not isinstance(other, (int, float)):
                raise ValueError("Expected an integer or floating-point value")
            return User(self.id * other, self.username * other)

        def __div__(self, other):
            if not isinstance(other, (int, float)):
                raise ValueError("Expected an integer or floating-point value")
            return User(self.id // other, self.username // other)

        def __mod__(self, other):
            if not isinstance(other, (int, float)):
                raise ValueError("Expected an integer or floating-point value")
            return User(self.id % other, self.username % other)

        def __and__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return User(self.id & other.id, self.username & other.username)

        def __or__(self, other):
            if not isinstance(other, User):
                raise ValueError("Expected a User instance")
            return User(self.id | other.id, self.username | other.username)

        def __pos__(self):
            return User(self.id, self.username)

        def __neg__(self):
            return User(-self.id, -self.username)

        def __abs__(self):
            return User(abs(self.id), abs(self.username))

        def __invert__(self):
            return User(~self.id, ~self.username)

        def __eq__(self, other, *args, **kwargs):
            if len(args) != 1:
                raise TypeError("Expected one argument")