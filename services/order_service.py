```python
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
        """
        Place a new order for a user.
        
        Args:
            user_id: The ID of the user placing the order.
            items: A list of item names to include in the order.
            total: The total cost of the order as a positive number.
        
        Returns:
            The created Order object.
        
        Raises:
            LookupError: If the user is not found.
            PermissionError: If the user is inactive.
            ValueError: If items are invalid or total is not positive.
            TypeError: If items contain non-string values.
        """
        user = _user_svc.get(user_id)
        if not user.is_active:
            raise PermissionError("Inactive users cannot place orders")
        validate_order_items(items)
        if total <= 0:
            raise ValueError("Order total must be positive")
        return _order_repo.insert(user, items, total)

    def get(self, order_id: int) -> Order:
        """
        Retrieve an order by its ID.
        
        Args:
            order_id: The ID of the order to retrieve.
        
        Returns:
            The Order object.
        
        Raises:
            LookupError: If the order is not found.
        """
        order = _order_repo.get_by_id(order_id)
        if not order:
            raise LookupError(f"Order {order_id} not found")
        return order

    def cancel(self, order_id: int) -> Order:
        """
        Cancel an existing order.
        
        Args:
            order_id: The ID of the order to cancel.
        
        Returns:
            The updated Order object with status set to CANCELLED.
        
        Raises:
            LookupError: If the order is not found.
            ValueError: If the order cannot be cancelled due to its current status.
        """
        order = self.get(order_id)
        if order.status not in (OrderStatus.PENDING, OrderStatus.CONFIRMED):
            raise ValueError(f"Cannot cancel order in status: {order.status.value}")
        _order_repo.update_status(order_id, OrderStatus.CANCELLED)
        return self.get(order_id)

    def list_for_user(self, user_id: int) -> list[Order]:
        """
        Retrieve all orders for a specific user.
        
        Args:
            user_id: The ID of the user.
        
        Returns:
            A list of Order objects for the user, which may be empty.
        
        Raises:
            LookupError: If the user is not found.
        """
        _user_svc.get(user_id)  # raises if not found
        return _order_repo.list_for_user(user_id)
```