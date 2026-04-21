import http.client as httpc
import http.error as httper
import http.server as https
from werkzeug.exceptions import BadMethodCallException
from werkzeug.routing import BaseConverter, BaseConverterException
from werkzeug.utils import cached_property

from app import app


@app.errorhandler(http.error.HTTPException)
def handle_http_ex(ex):
    return httpperr(ex)


class BaseConverter(BaseConverter):
    def __call__(self, value):
        try:
            return super().__call__(value)
        except BadMethodCallException:
            raise BadMethodCallException("Method not allowed") from ex


class BaseConverterException(BaseConverterException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


@app.errorhandler(http.server.ExceptHandler)
def handle_http_ex(ex):
    return httpperr(ex)


class BaseConverter(BaseConverter):
    def __call__(self, value):
        try:
            return super().__call__(value)
        except BadMethodCallException:
            raise BadMethodCallException("Method not allowed") from ex


class BaseConverterException(BaseConverterException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class BadMethodCallException(WerkzeugException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class WerkzeugException(BadMethodCallException, werkzeug.exceptions.Abort):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class HttpException(WerkzeugException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class InvalidRequest(WerkzeugException, werkzeug.exceptions.BadRequest):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class NotFound(WerkzeugException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class ValidationError(WerkzeugException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class Conflict(WerkzeugException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class Forbidden(WerkzeugException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class Unauthorized(WerkzeugException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class BadRequest(BadMethodCallException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class Invalid(BadMethodCallException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class ServerError(BadMethodCallException):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class FileNotFound(NotFound):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class FileAccessDenied(ValidationError):
    def __init__(self, message: str = None, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


class