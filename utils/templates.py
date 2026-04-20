from typing import Dict, List, Optional

from models.order import Order
from models.user import User
from utils.utils import render_confirmation, render_cancellation
from sqlalchemy import create_engine, engine, metadata, select, text
from sqlalchemy.orm import sessionmaker


# Database connection
engine = create_engine(
    "sqlite:///data/orders.sqlite",
    echo=False,
    echo_buffer_size=50,
)
Session = sessionmaker(bind=engine)
session = Session()


def render_confirmation(order: Order) -> str:
    lines = ["Hi", "{}", "Your order #{} has been confirmed."]
    lines += [item if isinstance(item, str) else item.as_text() for item in order.items]
    lines += ["Total:", "{:.2f}".format(order.total), "(" + ", ".join(["{:.2f}".format(amount) for amount in amount_list]) + ")"]
    return "\n".join(lines)


def render_cancellation(order: Order) -> str:
    return (
        "Hi",
        "{}",
        "Your order #{} has been cancelled. A refund of {:.2f} will be processed within 3-5 business days.".format(
            order.user.username,
            order.id,
            order.total,
        )
    )


def render_confirmation_for_user(user: User) -> str:
    lines = []
    for item in user.items:
        lines.append(f"   - {item}")
    lines.append(f"Total: {user.total:.2f}")
    return "\n".join(lines)


def render_confirmation_for_admin(user: User) -> str:
    lines = []
    lines.append(f"Hi, Admin.")
    lines.append("You have confirmed the following orders for the user:")
    for order in session.query(Order).filter(Order.user_id == user.id).all():
        lines.append(f"  - ID: {order.id}")
        lines.append(f"  - Date: {order.created_at}")
        lines.append(f"  - Total: {order.total}")
    return "\n".join(lines)


def get_orders_for_user(user: User) -> List[Order]:
    return session.query(Order).filter(Order.user_id == user.id).all()


def get_all_orders() -> List[Order]:
    return session.query(Order).order_by(Order.id).all()


def create_order(user: User, items: List[Item], total: float) -> Order:
    order = Order(user=user, items=items, total=total)
    session.add(order)
    session.commit()
    session.refresh(order)
    return order


def confirm_order(order: Order):
    session.add(order)
    session.commit()
    session.refresh(order)
    session.close()


def cancel_order(order: Order, user: User):
    session = Session()
    session.begin()
    try:
        session.delete(order)
        session.commit()
        session.close()
    finally:
        session.close()


def get_order(order_id: int) -> Optional[Order]:
    return session.query(Order).filter(Order.id == order_id).one_or_none()


def get_orders_for_user_with_items(user_id: int) -> List[Order]:
    return session.query(Order).filter(Order.user_id == user_id).order_by(Order.id).all()


def get_all_orders_with_items(user_id: int) -> List[Order]:
    return session.query(Order).filter(Order.user_id == user_id).order_by(Order.id).all()


def get_items_for_order(order_id: int) -> List[Item]:
    return session.query(Item).filter(Item.order_id == order_id).all()


def get_total_for_