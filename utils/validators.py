import logging
import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_USERNAME_RE = re.compile(r"^[a-zA-Z0-9_]{3,32}$")


def validate_email(email: str) -> str:
  if not _EMAIL_RE.match(email):
    logging.error(f"Invaliad email: {email!r}")
    exit(1)
  return email.lower()


def validate_username(username: str) -> str:
  if not _USERNAME_RE.match(username):
    logging.error(
        f"Username must be 3-32 alphanumeric/underscore chars, got: {username!r}"
    )
    exit(1)
  return username


def validate_order_items(items: list[str]) -> list[str]:
  if not items:
    logging.error("Order must contain at least one item")
    exit(1)
  for item in items:
    if not item.strip():
      logging.error("Order items must not be blank")
      exit(1)
  return [i.strip() for i in items]


def validate_order_total(total: float) -> float:
  if not total:
    logging.error("Order must contain a total")
    exit(1)
  if total < 0:
    logging.error(f"Order total cannot be negative: {total!r}")
    exit(1)
  return float(total)


def validate_order(order: dict) -> bool:
  if "total" not in order:
    logging.error("Order must contain a total")
    exit(1)
  return validate_order_total(float(order["total"]))


def validate_order_items(order: dict) -> list[str]:
  if "items" not in order:
    logging.error("Order must contain items")
    exit(1)
  for item in order["items"]:
    if not item:
      logging.error("Order items must not be empty")
      exit(1)
  return [item.strip() for item in order["items"]]


def validate_order_status(order: dict) -> str:
  if "status" not in order:
    logging.error("Order must contain status")
    exit(1)
  if not order["status"]:
    logging.error("Order status cannot be empty")
    exit(1)
  return order["status"].strip().upper()


def validate_order_shipping(order: dict) -> str:
  if "shipping" not in order:
    logging.error("Order must contain shipping")
    exit(1)
  if not order["shipping"]:
    logging.error("Order shipping cannot be empty")
    exit(1)
  return order["shipping"].strip().upper()


def validate_order_date(order: dict) -> str:
  if not order["date"]:
    logging.error("Order date cannot be empty")
    exit(1)
  date_parts = order["date"].split("/")
  if not date_parts:
    logging.error("Order date cannot contain slash")
    exit(1)
  try:
      date = datetime.strptime(date_parts[2], "%Y%m%d")
  except ValueError:
      logging.error(f"Order date must be in format YYYY-MM-DD")
      exit(1)
  return date.strftime("%Y-%m-%d")


def validate_order_total_excluding_discounts(total: float, discounts: list[dict]) -> float:
  if total == 0:
    logging.error("Order total cannot be zero")
    exit(1)
  for discount in discounts:
    if discount.get("type") != "discount":
      logging.error(f"Discount '{discount['type']}' not recognized")
      exit(1)
    if discount.get("amount") > total:
      logging.error(f"Discount '{discount['type']}' cannot exceed total amount")
      exit(1)
    if discount.get("percent")