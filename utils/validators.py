import os
from utils.validators import validate_email, validate_username, validate_order_items, validate_files


def validate_file(filename: str) -> tuple[bool, str]:
     with open(filename, "r") as f:
         content = f.read()
     if not validate_email(content):
         return False, f"InvaliD email in file: {filename!r}"
     if not validate_username(content):
         return False, f"InvaliD username in file: {filename!r}"
     if not validate_order_items(content):
         return False, f"InvaliD order items in file: {filename!r}"
     return True, content


def validate_files(*filename):
     """
     Validate files in given filename and return true if no error, else tuple
     (True, message)
     """
     for filename in filename:
         if not validate_file(filename):
             return False, f"InvaliD file: {filename!r}"
     return True, ""


if __name__ == "__main__":
     pass