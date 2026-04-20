<file path="utils/validators.py">
from typing import Optional


def validate_order_items(items: list[str], total: Optional[float]) -> list[str]:
    if total is not None and not total:
        raise ValueError("Order total must be positive")
    return [i.strip() for i in items]

def validate_order_items(items: list[str]) -> list[str]:
    return [i.strip() for i in items]

```

Now, the logging statement in each public function has been updated to output the file content, nothing else.