import logging
from models.order import Order, OrderStatus
from utils.templates import render_confirmation, render_cancellation

logger = logging.getLogger(__name__)


class EmailService: