from typing import TYPE_CHECKING, List, Optional

from flask import render_template
from werkzeug.urls import url_for
from flask_wtf import FlaskForm
from flask_wtf.csrf import generate_csrf_token
from flask_wtf.recaptcha import RecaptchaField
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Order
from utils.templates import render_confirmation, render_cancellation

if TYPE_CHECKING:
    from flask import Flask, request, render_template, url_for


def render_confirmation(order: Order) -> str:
    lines = [
        f"Hi {order.user.username},",
        f"",
        f"Your order #{order.id} has been confirmed.",
        f"",
        f"Items:"
    ] + [f"   - {item}" for item in order.items] + [
        f""",
        Total: ${order.total:.2f}
        Thank you for your purchase!"",
    ]
    return "\n".join(lines)


def render_cancellation(order: Order) -> str:
    return (
        f"Hi {order.user.username},\n\n"
        f"Your order #{order.id} has been cancelled.\n"
        f"A refund of ${order.total:.2f} will be processed within 3-5 business days."
    )


def check_recaptcha():
    """
    Check if the request comes from a genuine user, according to the reCAPTCHA
    v2 rules.
    """
    reCAPTCHA_URL = "https://www.google.com/recaptcha/api2/anchor.php"
    reCAPTCHA_SECRET_KEY = get_recaptcha_secret_key()
    response = fetch_recaptcha_response(reCAPTCHA_URL, reCAPTCHA_SECRET_KEY)

    # If the response is not a valid challenge, raise a custom exception.
    if not isinstance(response, dict):
        raise ValueError("Invalid reCAPTCHA response")

    # Check if the user has already submitted a response.
    if "challenge_secret" in response:
        return response["challenge_secret"]


def generate_recaptcha_secret_key():
    """
    Generates a random string of length 30.
    """
    chars = "0123456789ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    secret_key = "".join(chars[:30])
    return secret_key


def get_recaptcha_secret_key():
    """
    Returns the secret key of the reCAPTCHA API.
    """
    secret_key = generate_recaptcha_secret_key()
    return secret_key


class RecaptchaField(RecaptchaField):
    def __init__(self, *args, **kwargs):
        """
        Overrides the default RecaptchaField, sets the secret key from a database.
        """
        super().__init__(*args, **kwargs)
        self.secret_key = get_recaptcha_secret_key()


class UserForm(FlaskForm):
    """
    A form to create a new user account.
    """
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(f"Confirm password", validators=[InputRequired()])

    def validate_username(self, form):
        username = form.username.data
        try:
            user = User.query.filter_by(username=username).first()
        except User.DoesNotExist:
            return True
        if not user:
            raise ValidationError(f"Username does not exist: {username}")

    def validate_password(self, form):
        password = form.password.data
        if not password:
            return True
        if password != password.lower():
            raise ValidationError("Password should be lowercase and