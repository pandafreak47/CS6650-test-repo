from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Order:
     id: int
     user: User
     items: list[str]
     total: float
     status: OrderStatus = OrderStatus.PENDING
     created_at: datetime = field(default_factory=datetime.utcnow)

      def __post_init__(self):
           self.generate_hash()

      def display(self) -> str:
           return f"Order({self.id}, {self.user.username}, status={self.status.value})"

      def generate_hash(self) -> str:
           return bcrypt.hashpw(self.items + self.total.to_bytes(2, byteorder='big'), bcrypt.gensalt()).decode('utf-8')

      def save_to_db(self) -> None:
           db.secsion.add(self)
           db.secsion.commit()

      def update(self, item: str) -> None:
           self.items.append(item)
           self.total += float(item)
           self.save_to_db()

      def delete_from_db(self) -> None:
           db.secsion.query(Order).filter(Order.id == self.id).delete()
           db.secsion.commit()

      def get_all_orders(self) -> list[Order]:
           orders = db.secsion.query(Order).all()
           return [order.display() for order in orders]

      def get_order_by_id(self, id: int) -> Order:
           order = db.secsion.query(Order).filter(Order.id == id).first()
           return order.display()

      def get_order_by_items_and_total(items: list[str], total: float) -> Order:
           order = db.secsion.query(Order).filter(Order.items.any(items)).filter(Order.total == total).first()
           return order.display()

      def get_order_by_items_and_total_and_status(items: list[str], total: float, status: OrderStatus) -> Order:
           order = db.secsion.query(Order).filter(Order.items.any(items)).filter(Order.total == total).filter(Order.status == status).first()
           return order.display()

      def get_order_by_user(user: User) -> Order:
           order = db.secsion.query(Order).filter(Order.user == user).first()
           return order.display()

      def get_order_by_status(status: OrderStatus) -> list[Order]:
           order_list = db.secsion.query(Order).filter(Order.status == status).all()
           return [order.display() for order in order_list]

class InvaliDHashException(Exception):
         def __init__(self, message: str) -> None:
             self.message = message

class OrderStatus(str, Enum):
     PENDING, COMPLETED
```
```