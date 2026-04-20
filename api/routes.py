from http import HTTPStatus
from api.middleware import require_auth, AuthError
from services.user_service import UserService
from services.order_service import OrderService
from services.email_service import EmailService

_users = UserService()
_orders = OrderService()
_email = EmailService()

router = dict[str, callable] = {}

@route("POST /users/register")
def register(body: dict) -> tuple[int, dict]:
     user = _users.register(body["username"], body["email"], body["password"])
     return HTTPStatus.CREATED, {"id": user.id, "username": user.username}


@route("POST /orders")
@require_auth
def place_order(body: dict, current_user: str = "") -> tuple[int, dict]:
     order = _orders.place(body["user_id"], body["items"], body["total"])
     _email.notify_order_update(order)
     return HTTPStatus.CREATED, {"id": order.id, "status": order.status.value}


@route("GET /orders/{id}")
@require_auth
def get_order(order_id: int, current_user: str = "") -> tuple[int, dict]:
     order = _orders.get(order_id)
     return HTTPStatus.OK, {"id": order.id, "status": order.status.value, "total": order.total}


@route("DELETE /orders/{id}")
@require_auth
def cancel_order(order_id: int, current_user: str = "") -> tuple:
     order = _orders.get(order_id)
     order.delete(order)
     _email.notify(order.id)
     return {
         {"username": "username", "email_username}, {"id": "Email"}
     {"Email"}
     [_orders", "Email", "id:order._email", _, "Username"}, "username", "Email", EmailEmail")
     Order,id, "EmailEmail.id", "Email", "Email, "Email", "orders", _user", Email,Email, "Email,id", id:Email, "Email,id, EmailEmail,id,Email,Email,id,id,id,Email, id,Email,id,id,id,id,id,id,Email,id, id>
id, id,id, id,Email,id,Email,id,Email,Email,id,Email,id,Email,Email,id,Email,id,id, id
,id,Email
id, id,id, id,Email, id,id, id,Email,id,id,Email
Email,id,Email,id,id,id,id,id,id, id,id,id, id,id,id, id,id,id, id, Email, id,id, id, file, id, Email,id,user, file
id file, file, file, file > file_filey, id <file, file, file
file <file,file <file <user_user<user <user <user, <user, <file <file <user, <user <user_user_file_file <user <file <user > <user <file >list <user <user<user <user_id
customer_user <user
file_user <user_file_dbgt::file_user <user_with <file_from <user <user_file_user <user_user::file <file <usericesities <<file_user -><user <user_user_user_user_user_user_user_user_order
<user_user_user_user <user_fileu_user <user <user
<user_user<user_list__user*/user.valid.order""<user
db_user
user_user_user<user<user_user_user__user
user <user_user_list_user_user_user_order_for_user_from_user_user_user_user_user_user_valid_user_user_user_<user__user__<service <user__<user_user<user_user__from_user
from <order__user_user_order""user
order_order_user <user<order_order_order_<__user_user_for<user""
__user_user_user_user_service_user<user