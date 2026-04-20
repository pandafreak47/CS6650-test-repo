from flask import render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .models import User

from werkzeug.security import generate_password_hash, check_password_hash

from .forms import LoginForm, RegistrationForm


def db_session(app):
    db = SQLAlchemy(app)
    db.create_all()
    return db


def login_manager(app):
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'
    login_manager.login_message_template = 'login.html'
    return login_manager


def form_errors(form):
    return f'Error: {form.errors.as_string()}'


def render_template(template, **kwargs):
    if 'form' not in kwargs:
        return render_template(template, **kwargs)
    else:
        form = kwargs['form']
        return render_template(template, form=form, **kwargs)


def render_confirmation(order: Order) -> str:
    lines = [
        f"Hi {order.user.username},",
        f"""
        Your order #{order.id} has been confirmed.
        Items:
        - {order.items}
        Total: ${order.total:.2f}
        Thank you for your purchase!
        """,
    ]
    return "\n".join(lines)


def render_cancellation(order: Order) -> str:
    return (
        f"Hi {order.user.username},\n\n"
        f"Your order #{order.id} has been cancelled. A refund of ${order.total:.2f} will be processed within 3-5 business days."
    )


def __all__ = ["render_confirmation", "render_cancellation"]


def render_confirmation(order: Order) -> str:
    lines = [
        f"Hi {order.user.username},",
        f"""
        Your order #{order.id} has been confirmed.
        Items:
        - {order.items}
        Total: ${order.total:.2f}
        Thank you for your purchase!
        """,
    ]
    return "\n".join(lines)


def __all__ = ["render_confirmation"]


def render_cancellation(order: Order) -> str:
    return (
        f"Hi {order.user.username},\n\n"
        f"Your order #{order.id} has been cancelled. A refund of ${order.total:.2f} will be processed within 3-5 business days."
    )


def __all__ = ["render_cancellation"]


def render_confirmation(order: Order) -> str:
    lines = [
        f"Hi {order.user.username},",
        f"""
        Your order #{order.id} has been confirmed.
        Items:
        - {order.items}
        Total: ${order.total:.2f}
        Thank you for your purchase!
        """
    ]
    return "\n".join(lines)


def __all__ = ["render_confirmation"]


def render_cancellation(order: Order) -> str:
    return (
        f"Hi {order.user.username},\n\n"
        f"Your order #{order.id} has been cancelled. A refund of ${order.total:.2f} will be processed within 3-5 business days."
    )


def __all__ = ["render_cancellation"]


def render_confirmation(order: Order) -> str:
    lines = [
        f"Hi {order.user.username},",
        f"""
        Your order #{order.id} has been confirmed.
        Items:
        - {order.items}
        Total: ${order.total:.2f}
        Thank you for your purchase!
        """
    ]
    return "\n".join(lines)


def __all__ = ["render_confirmation"]


def render_cancellation(order: Order) -> str:
    return (
        f"Hi {order.user.username},\n\n"
        f"Your order #{order