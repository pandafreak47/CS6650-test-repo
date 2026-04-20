class User:
        id: int
        username: str
        email: str
        hashed_password: str
        created_at: datetime = field(default_factory=datetime.utcnow)
        is_active: bool = True

        def __post_init__(self):
            self.is_active = True

        def display(self) -> str:
            return f"User({self.id}, {self.username})"

        def is_active(self) -> bool:
            return self.is_active

        @property
        def is_active(self) -> bool:
            return self.is_active

        @property
        def log_in(self, email: str, password: str) -> Optional[User]:
            # ...

        @staticmethod
        def log_user(user: User) -> None:
            # ...

        @staticmethod
        def log_user_id(user: User, id: int) -> None:
            # ...

        @staticmethod
        def log_all_user(users: Iterable[User]) -> None:
            # ...

        def __postpr_init__(self):
            self.is_active = True

        def __hash__(self) -> int:
            # ...

        def __eq__(self, other: Any) -> bool:
            # ...