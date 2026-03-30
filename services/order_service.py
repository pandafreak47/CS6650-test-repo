from db.user_repo import UserRepo
from db.order_repo import OrderRepo
from models.order import Order, OrderStatus
from services.user_service import UserService
from utils.validators import validate_order_items

_user_repo = UserRepo()
_order_repo = OrderRepo(_user_repo)
_user_svc = UserService()


class OrderService:
    def place(self, user_id: int, items: list[str], total: float) -> Order:
        user = _user_svc.get(user_id)
        if not user.is_active:
            raise PermissionError("Inactive users cannot place orders")
        validate_order_items(items)
        if total <= 0:
            raise ValueError("Order total must be positive")
        return _order_repo.insert(user, items, total)

    def get(self, order_id: int) -> Order:
        order = _order_repo.get_by_id(order_id)
        if not order:
            raise LookupError(f"Order {order_id} not found")
        return order

    def cancel(self, order_id: int) -> Order:
        order = self.get(order_id)
        if order.status not in (OrderStatus.PENDING, OrderStatus.CONFIRMED):
            raise ValueError(f"Cannot cancel order in status: {order.status.value}")
        _order_repo.update_status(order_id, OrderStatus.CANCELLED)
        return self.get(order_id)

    def list_for_user(self, user_id: int) -> list[Order]:
        _user_svc.get(user_id)  # raises if not found
        return _order_repo.list_for_user(user_id)
