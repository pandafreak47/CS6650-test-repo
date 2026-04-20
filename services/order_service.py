class OrderService:
     def __init__(self, user_repo):
         self.user_repo = user_repo

     def get_order_by_id(self, order_id: int) -> Order:
         row = self.user_repo.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
         if row:
             user = self.user_repo.get_by_id(row["user_id"])
             return _row_to_order(row, user)
         return None

     def list_for_user(self, user_id: int) -> list[Order]:
         rows = self.user_repo.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
         user = self.user_repo.get_by_id(user_id)
         return [_row_to_order(row, user) for row in rows]

     def cancel(self, order_id: int):
         row = self.user_repo.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
         if row:
             order = _row_to_order(row)
             self.user_repo.update_status(order_id, OrderStatus.CANCELLED)
             return order
         return None

     def list_for_user(self, user_id: int) -> list[Order]:
         rows = self.user_repo.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
         order_ids = [row["id"] for row in rows]
         return [_row_to_order(row) for row in rows]

     def insert(self, order_id: int, user_id: int, items: list[str], total: float):
         # Your code
         pass

     def get_by_id(self, order_id):
         # Your code
     def get_user(user_id:json.json):
         # Your code
     def get(user_id):
         pass
         # code:json:json)
         # 
         user:
         user, json:
         total:
         # id)
         # Your json:
user:
        
         # user_id:json:json
         # user:json:json:
json:
         # User
# json:json:

#id


id |id:json:
id


user,user |user |id |user_user |json>user |user >user
id
user_user_user
#id, user






user, user
user, user
user
user, u
user
#user, user
user_user:id:user,user, u, user, user |id
user #user
id
user |user
user, id,
user, user,user, id, id, id
user|id |id |id #
id
user | user, ... |user, __for,y |user, #fileydpid #id #user,idid:user |user:filep:row |file |file
file =uid
user,user_from_user
user,user
user,user,filepy
id.user_userient_user_user_project
from_user_user_file_file
file_user_user_user__user_user_file.user
user__file_user_project.____user_user__user_user =file =__user_user_user_user_from_from =from_db_user_filter_with_to_file_project(from_json_mut__user_user_date_database_file__project._______________exec_user_list_database__from__<db__json__user_user_project_user_user_user__dict_user_database_cursor_data__file_model_users_with__from__data_from__user_user.filter__user__user__from__from_user_from_db__fromdb_user_user_db_user_user_mut_user____user__with_user_db_database_list_list_user_user_user =<user__from____from_user_list_user_user_fromuser_from_from_from_date.from
json_dis_from_from""<fromdbuser_user__user.from__user