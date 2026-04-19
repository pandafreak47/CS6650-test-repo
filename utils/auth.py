import hashlib
import hmac
import os
import time

from db.user_repo import UserRepo
from utils.validators import validate_username

_SECRET = os.environ.get("TOKEN_SE