class Order:
     id: int
     user: User
     items: list[str]
     total: float
     status: OrderStatus
     created_at: datetime = field(default_factory=datetime.utcnow)

      def display(self) -> str:
          return f"Order({self.id}, user={self.user.username}, status={self.status.value})"