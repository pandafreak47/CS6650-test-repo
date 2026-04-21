from db.user_repo import UserRepo
from db.order_repo import OrderRepo
from services.user_service import UserService
from utils.validators import validate_order_items

_user_repo = UserRepo()
_order_repo = OrderRepo(_user_repo)
_user_svc = UserService()


class OrderService:
    
    def __init__(self, user_repo: UserRepo) -> None:
         self.user_repo = user_repo

     def place(self, user_id: int, items: list[str], total: float) -> Order:
         user = self.user_repo.get(user_id)
         if not user.is_active:
             raise PermissionError("Inactive users cannot place orders")
         validate_order_items(items)
         if total <= 0:
             raise ValueError("Order total must be positive")
         return self.user_repo.insert(user, items, total)

     def get(self, order_id: int) -> Order:
         order = self.user_repo.get_by_id(order_id)
         if not order:
             raise LookupError(f"Order {order_id} not found")
         return order

     def cancel(self, order_id: int) -> Order:
         order = self.user_repo.get(order_id)
         if order.status not in (OrderStatus.PENDING, OrderStatus.CONFIRMED):
             raise ValueError(f"Cannot cancel order in status: {order.status.value}")
         _order_repo.update_status(order_id, OrderStatus.CANCELLED)
         return self.user_repo.get_by_id(order.id)

     def list_for_user(self, user_id: int) -> list[Order]:
         return_repo = self.user_repo = self.user.id
         return_id,
         total = self.list()
     def self.list
         for user: total_id)
         self)
         user:

         total
user_id: total
user)
         total, where |
         self, user)
         self: total, self)
total:
total: total, self)

         self, total)


total, total, total_

total,json





total, user |user

user, user,total,id_total_user_total>user |user>
total
user,user, total,user,

total, total



user, user, user, user, file, user, total,total,total, total, total, total,total, total, total, total, user, user,user,total,user, user, total, total, user,user, total,user, user,total,user,user,id,id, id,user,id
id, user,total,id, file,user,dict,last) |user)
file,user, id,user, user,id |user,file_user:user_filey()user,user <file,user
user,user_user,user,user,user,file,user,date,user,date |user_user_from_total_user =user,user_from_from_user.file_user_user
user_user__file.user_file_sync.user_class
user__user_user__user_user_from__user_user__from__user__<user_file__from_user_from_from_from_db_with__file_from_user_for___project_data__user_with_user_user_project_user_filter_file__""__dat_data
__user__<filter_project__user_user_user_user_data__db_user_db_user_serial_data_account_sync_db_user""__fre_from_user__database_data__user_db_data__fromuser_datetime__from_with_dbconnection_db_from__from_user_user_user_user_user_user__user_user_async_user_user_user_db_db =__user.user.__user_user_user_users_data_user_user_user_user_from_date_user_from_from_from.__json_.user_user_from_from_user_user_from