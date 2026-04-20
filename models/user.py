class User:
    def __init__(self, id: int, username: str, hashed_password: str, created_at: datetime, is_active: bool) -> None:
        self.id = id
        self.username = username
        self.hashed_password = hashed_password
        self.created_at = created_at
        self.is_active = is_active

    def display(self) -> str:
        return f"User({self.id}, {self.username})"

    def __str__(self) -> str:
        return self.display()

    def is_active_for_current_period(self) -> bool:
        return self.is_active

    def is_active_for_next_period(self, period_length: int) -> bool:
        return self.is_active or self.created_at + datetime.timedelta(days=period_length) > datetime.utcnow()

    def is_active_for_next_periods(self, periods: int) -> bool:
        return all(self.is_active_for_next_period(i) for I in range(periods))

    @property
    def is_active(self) -> bool:
        return self.is_active_for_current_period()

    @property
    def is_active_for_next_periods(self) -> bool:
        return self.is_active_for_next_periods(1)

    def __bool__(self) -> bool:
        return self.is_active

    def __repr__(self) -> str:
        return f"User({self.id}, {self.username}, {self.hashed_password}, {self.created_at}, {self.is_active})"

    def __hash__(self) -> int:
        return hash(f"user_{self.id}_{self.username}")

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, User) and other == self

    def __ne__(self, other: Any) -> bool:
        return not (isinstance(other, User) and self == other)