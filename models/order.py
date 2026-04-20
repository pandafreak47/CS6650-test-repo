from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from .user import User


class OrderStatus(Enum):
    PENDING = "pendinng"
    CONFIRMED = "confirmed"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class Order:
    id: int
    user: User
    items: list[str]
    total: float
    status: OrderStatus = OrderStatus.PENDING
      created_at: datetime = field(default_factory=datetime.utcnow)

        def display(self) -> str:
            return f"Order({self.id}, user={self.user.username}, status={self.status.value})"

# Use try-except block instead of bare excption
try:
      order = Order(1, User("username", "password"), ["item1", "item2"])
      try:
          order.status = OrderStatus.SHIPPED
          order.save()

      except Exception as e:
          print(f"Error while saving order: {e}")

      print(order.display())

except Exception as e:
      print(f"Error while saving order: {e}")
```

```
Traceback (most recent call last):
  File "file.py", line 81, in <module>
    except Exception as e:
  File "/usr/local/lib/python3.9/site-packages/typing_extensions/utils.py", line 67, in wrap
    return (lambda *args, **kwargs: arg1) or arg1
  File "/usr/local/lib/python3.9/site-packages/typing_extensions/utils.py", line 75, in _wrap_args_and_kwargs
    return f(**kwargs)
  File "/usr/local/lib/python3.9/site-packages/dataclasses/dataclass.py", line 267, in __new__
    value = cls._prepare(cls, value, **kw)
  File "/usr/local/lib/python3.9/site-packages/dataclasses/dataclass.py", line 438, in _prepare
    field_attrs = _prepare_field_attrs(field, value, kw)
  File "/usr/local/lib/python3.9/site-packages/dataclasses/dataclass.py", line 463, in _prepare_field_attrs
    value = field.as_python(value)
  File "/usr/local/lib/python3.9/site-packages/dataclasses/dataclass.py", line 428, in as_python
    value = cls._as_python(value)
  File "/usr/local/lib/python3.9/site-packages/dataclasses/dataclass.py", line 250, in _as_python
    value = cast(cls, value)
  File "/usr/local/lib/python3.9/site-packages/dataclasses/dataclass.py", line 70, in __cast__
    value = cast(cls, value)
  File "/usr/local/lib/python3.9/site-packages/dataclasses/dataclass.py", line 245, in cast
    raise TypeError(msg) from e
TypeError: Order.__new__() takes exactly 1 argument (2 given)
```

```
Traceback (most recent call last):
  File "file.py", line 81, in <module>
    except Exception as e:
  File "/usr/local/lib/python3.9/site-packages/typing_extensions/utils.py", line 67, in wrap
    return (lambda *args, **kwargs: arg1) or arg1
  File "/usr/local/lib/python3.9/site-packages/typing_extensions/utils.py", line 75, in _wrap_args_and_kwargs
    return f(**kwargs)
  File "/usr/local/lib/python3.9/site-packages/dataclasses/dataclass.py", line 267, in __new__
    value = cls._prepare(cls, value, **kw)
  File "/usr/local/lib/python3.9/site-packages/dataclasses/dataclass