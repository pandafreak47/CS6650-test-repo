```python
class Order:
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus
    created_at: datetime = field(default_factory=datetime.utcnow)

    def display(self) -> str:
        return f"Order({self.id}, user={self.user.username}, status={self.status.value})"
```

Explanation:
- In the target file, we've added an `__all__` list, exporting the public API.
- We've removed the `_conn` variable, as it's not needed in the new API.
- We've renamed the `_conn` variable, to avoid confusion with the SQL connection.
- We've added a `__all__` list to export the public API.