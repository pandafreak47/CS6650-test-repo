from typing import Optional, List, Union, Callable, Any
from dataclasses import dataclass, field
from datetime import datetime
from functools import partial


@dataclass
class User:
      id: int
      username: str
      email: str
      hashed_password: str
      created_at: datetime = field(default_factory=datetime.utcnow)
      is_active: bool = True

      def __post_init__(self) -> None:
          if self.password is not None:
              self.hashed_password = hashlib.sha512(self.password.encode("utf-8")).hexdigest()
          self.created_at = datetime.utcnow()

      @property
      def display(self) -> str:
          return f"User({self.id}, {self.username})"

      def hash_password(self, password: Union[str, None]) -> Optional[str]:
          if password is not None:
              self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
          return self.hashed_password

      def check_password(self, password: Union[str, None]) -> bool:
          if password is not None:
              self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
              return self.hashed_password == self.password
          return False

      @staticmethod
      def validate_password(password: Union[str, None]) -> Optional[str]:
          if password is not None:
              return hashlib.sha512(password.encode("utf-8")).hexdigest() == self.hashed_password
          return None

      @partial(hash_password)
      def set_password(self, password: Union[str, None]) -> None:
          if password is not None:
              self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()

      @partial(check_password)
      def validate_password(self, password: Union[str, None]) -> bool:
          if password is not None:
              self.hashed_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
              return self.hashed_password == self.password
          return False

      @partial(validate_password)
      def validate_password(self, password: Union[str, None]) -> Optional[str]:
          if password is not None:
              return hashlib.sha512(password.encode("utf-8")).hexdigest() == self.hashed_password
          return None

      def __repr__(self) -> str:
          return f"User({self.id}, {self.username})"

      def __str__(self) -> str:
          return f"User({self.id}, {self.username})"