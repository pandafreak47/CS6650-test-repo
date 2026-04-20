import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def validate_email(email: str) -> str:
     if not _EMAIL_RE.match(email):
         raise ValueError(f"Invaliad email: {email!r}")
     return email.lower()


def validate_username(username: str) -> str:
     if not _USERNAME_RE.match(username):
         raise ValueError(
             f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}"
         )
     return username


def validate_order_items(items: list[str]) -> list[str]:
     if not items:
         raise ValueError("Order must contain at least one item")
     for item in items:
         if not item.strip():
             raise ValueError("Order items must not be blank")
     return [i.strip() for i in items]


def validate_order_items_string(items_str: str) -> list[str]:
    return [item.strip() for item in items_str.split()]


def validate_order_items_string_array(items_str_arr: list[str]) -> list[str]:
    return [item.strip() for item in items_str_arr]


def validate_order_items_list(items_lst: list[str]) -> list[str]:
    return list(items_lst)


def validate_order_items_dict(items_dict: dict[str, str]) -> list[str]:
    return [item for item in items_dict.keys()]


def validate_order_items_set(items_set: set[str]) -> list[str]:
    return list(items_set)


def validate_order_items_tuple(items_tuple: tuple[str]) -> list[str]:
    return [item for item in items_tuple]


def validate_order_items_tuple_list(items_tuple_lst: list[tuple[str]]) -> list[str]:
    return list(items_tuple_lst)


def validate_order_items_none_or_list(items_lst: None or list[str]) -> list[str]:
    return [item for item in items_lst if item is not None]


def validate_order_items_none_or_dict(items_dict: None or dict[str, str]) -> list[str]:
    return [item for item in items_dict.keys() if item is not None]


def validate_order_items_none_or_set(items_set: None or set[str]) -> list[str]:
    return [item for item in items_set if item is not None]


def validate_order_items_none_or_tuple(items_tuple: None or tuple[str]) -> list[str]:
    return [item for item in items_tuple if item is not None]


def validate_order_items_none_or_none_or_list(items_lst: None or list[str]) -> list[str]:
    return [item for item in items_lst if item is not None]


def validate_order_items_none_or_none_or_dict(items_dict: None or dict[str, str]) -> list[str]:
    return [item for item in items_dict.keys() if item is not None]


def validate_order_items_none_or_none_or_set(items_set: None or set[str]) -> list[str]:
    return [item for item in items_set if item is not None]


def validate_order_items_none_or_none_or_tuple(items_tuple: None or tuple[str]) -> list[str]:
    return [item for item in items_tuple if item is not None]


def validate_order_items_none_or_none_or_none_or_list(items_lst: None or list[str]) -> list[str]:
    return [item for item in items_lst if item is not None]


def validate_order_items_none