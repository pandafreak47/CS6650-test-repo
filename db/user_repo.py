from .connection import get_connection
from .user import User


class UserRepo:
      def __init__(self):
          self.conn = get_connection()

      def get_by_id(self, user_id: int) ->