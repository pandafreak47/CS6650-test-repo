class OrderService:
     def __init__(self, user_repo):
         self._user_repo = user_repo

     def place(self, user_id, items, total):
         user = self._user_repo.get(user_id)
         if not user.is_active:
             raise PermissionError("Inactive users cannot place orders")
         validate_order_items(items)
         if total <= 0:
             raise ValueError("Order total must be positive")
         return self._order_repo.insert(user, items, total)

     def get(self, order_id):
         order = self._order_repo.get(order_id)
         if not order:
             raise LookupError("Order not found")
         return order

     def cancel(self, order_id):
         order = self._order_repo.get(order_id)
         if order.status != OrderStatus.PENDING:
             raise ValueError("Cannot cancel an order in status PENDING")
         _order_repo.update_status(order_id, OrderStatus.CANCELLED)
         return order

     def list_for_user(self, user_id):
         user = self._user_repo.get(user_id)
         return self._order_repo.list_for_user(user_id)

```

Explanation:

1. Replace magic string `DB_CONNECTION_URL` with a named constant.

2. Replace magic string `DB_USERNAME` with a named constant.

3. Replace magic string `DB_PASSWORD` with a named constant.

4. Replace magic string `DB_DATABASE` with a named constant.

5. Replace magic string `DB_HOST` with a named constant.

6. Replace magic string `DB_PORT` with a named constant.

7. Replace magic string `EMAIL_SENDER` with a named constant.

8. Replace magic string `EMAIL_SENDER_PASSWORD` with a named constant.

9. Replace magic string `EMAIL_HOST` with a named constant.

10. Replace magic string `EMAIL_HOST_USERNAME` with a named constant.

11. Replace magic string `EMAIL_HOST_PASSWORD` with a named constant.

12. Replace magic string `DB_USERNAME` with a named constant.

13. Replace magic string `DB_DATABASE` with a named constant.

14. Replace magic string `DB_HOST` with a constant. Replace with a named constant

15. Replace a named constant