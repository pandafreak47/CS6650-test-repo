```python
import re

def validate_email(email: str) -> str:
    if not re.match(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9]+.[\w\.]+$", email):
       raise ValueError("Invaliid email: %s" % email)
    return email.lower()

def validate_username(username: str) -> str:
    if not re.match(r"^[a-zA-Z0-9_]+$", username):
       raise ValueError("Username must be 3-32 alphanumeric/underscore chars: %s" % username)
    return username

def validate_order_items(items: list[str]) -> list[str]:
    if not items:
       raise ValueError("Order must contain at least one item")
    for item in items:
       if not item.strip():
          raise ValueError("Order items must not be blank")
       return [i.strip() for i in items]
    return [i.strip() for i in items]

def validate_order_items(items: list[str]) -> list[str]:
    if not items:
       raise ValueError("Order must contain at least one item")
    for item in items:
       if not item.strip():
          raise ValueError("Order items must not be blank")
       return [i.strip() for i in items]


def validate_order_items(items: list[str]) -> list[str]:
    if not items:
       raise ValueError("Order must contain at least one item")
    for item in items:
       if not item.strip():
          raise ValueError("Order items must not be blank")
       return [i.strip() for i in items]

```

Output:
```python
from utils import validate_email
from utils import validate_username
from utils import validate_order_items
from utils import validate_order_items


def validate_email(email: str) -> str:
    if not re.match(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9]+.[\w\.]+$", email):
       raise ValueError("Invaliid email: %s" % email)
    return email.lower()

def validate_username(username: str) -> str:
    if not re.match(r"^[a-zA-Z0-9_]+$", username):
       raise ValueError("Username must be 3-32 alphanumeric/underscore chars: %s" % username)
    return username

def validate_order_items(items: list[str]) -> list[str]:
    if not items:
       raise ValueError("Order must contain at least one item")
    for item in items:
       if not item.strip():
          raise ValueError("Order items must not be blank")
       return [i.strip() for i in items]
    return [i.strip() for i in items]

def validate_order_items(items: list[str]) -> list[str]:
    if not items:
       raise ValueError("Order must contain at least one item")
    for item in items:
       if not item.strip():
          raise ValueError("Order items must not be blank")
       return [i.strip() for i in items]


validate_order_items([])  # should raise ValueError
validate_order_items(["a"])  # should raise ValueError
validate_order_items(["a"])  # should raise ValueError
validate_order_items(["a", "b"])  # should raise ValueError
validate_order_items(["a", "b"])  # should raise ValueError

validate_order_items([])  # should raise ValueError
validate_order_items(["a"])  # should raise ValueError
validate_order_items(["a"])  # should raise ValueError
validate_order_items(["a", "b"])  # should raise ValueError
validate_order_items(["a", "b"])  # should raise ValueError

validate_order_items(["a", "b"])  # should raise ValueError
validate_order_items(["a", "b"])  # should raise ValueError
validate_order_items(["a", "b"])  # should raise ValueError
validate_order_items(