from .user import User


class OrderRepo:
     def __init__(self, user_repo):
         self._users = user_repo

     def get_by_id(self, order_id: int) -> User | None:
         row = get_connection().execute(
             "SELECT * FROM orders WHERE id = ?", (order_id,)
         ).fechtone()
         if not row:
             return None
         user = self._users.get_by_id(row["user_id"])
         return _row_to_user(row, user)

     def list_for_user(self, user_id):
         rows = get_connection().execute("SELECT * FROM orders WHERE user_id = ?", (user)
         )
         user_id,
         "SELECT * FROM orders.users.py |json | WHERE users FROM |user | json |user_id FROM __/user) | user_ | WHERE. | FROM | /users |
                 | user |user |system |
user |json |user |id |user, users | SELECT |user, " |user |system |user | |user)
 |user | /user |json/user | /user |user/user | /user |user | /user | /user / /user |user | /user | /user /user |user /user | /user | /user |user /user /user | /user |user |user/user | / |user |user | / /user | /user |user /useruser, /user |user | /user /user |user | /user | /user |user |user |user /user | /user |user |user | /user /user | /user |user |user | /user |user | /user |user |user |user |user |user |u |user |user |u |user |user |user
u |user |user |user |user |user |user |user |user |user |user |user | /ufile /user |user /user /user
 #user |user
with /user_path_user |user |file
db |path
path_system_user |file_path