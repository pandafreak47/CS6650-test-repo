```python
"""
Entry point for the Order Management Service.

Starts a minimal HTTP server that dispatches to api/routes.py.
Run:  python main.py
"""
import json
import logging
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus

from api.routes import router
from api.middleware import AuthError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

# Configuration constants
DEFAULT_PORT = 8080
PORT_ENV_VAR = "PORT"
HOST = "0.0.0.0"
CONTENT_TYPE_JSON = "application/json"
CONTENT_LENGTH_HEADER = "Content-Length"
CONTENT_TYPE_HEADER = "Content-Type"
AUTHORIZATION_HEADER = "Authorization"
EMPTY_STRING = ""
NOT_FOUND_ERROR = "Not found"

# HTTP method constants
GET_METHOD = "GET"
POST_METHOD = "POST"
DELETE_METHOD = "DELETE"

# Route path delimiters and formats
ROUTE_DELIMITER = " "

# Server constants
LOCALHOST = "0.0.0.0"
LOG_PORT_MESSAGE = "Listening on port %d"
LOG_REQUEST_FORMAT = "%s - %s"

# JSON encoding constants
JSON_ENCODING = "utf-8"

PORT = int(os.environ.get(PORT_ENV_VAR, DEFAULT_PORT))


class Handler(BaseHTTPRequestHandler):
    def _dispatch(self, method: str):
        body = {}
        if self.headers.get(CONTENT_LENGTH_HEADER):
            body = json.loads(self.rfile.read(int(self.headers[CONTENT_LENGTH_HEADER])))

        token = self.headers.get(AUTHORIZATION_HEADER, EMPTY_STRING)
        route_key = f"{method}{ROUTE_DELIMITER}{self.path}"
        handler = router.get(route_key)
        if handler is None:
            self._respond(HTTPStatus.NOT_FOUND, {"error": NOT_FOUND_ERROR})
            return

        try:
            if method == POST_METHOD:
                status, data = handler(body, token=token)
            else:
                status, data = handler(token=token)
            self._respond(status, data)
        except AuthError as e:
            self._respond(HTTPStatus.UNAUTHORIZED, {"error": str(e)})
        except (LookupError, ValueError) as e:
            self._respond(HTTPStatus.BAD_REQUEST, {"error": str(e)})

    def do_GET(self):
        self._dispatch(GET_METHOD)

    def do_POST(self):
        self._dispatch(POST_METHOD)

    def do_DELETE(self):
        self._dispatch(DELETE_METHOD)

    def _respond(self, status: HTTPStatus, data: dict):
        body = json.dumps(data).encode(JSON_ENCODING)
        self.send_response(status.value)
        self.send_header(CONTENT_TYPE_HEADER, CONTENT_TYPE_JSON)
        self.send_header(CONTENT_LENGTH_HEADER, len(body))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        logger.info(LOG_REQUEST_FORMAT, self.address_string(), fmt % args)


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    logger.info(LOG_PORT_MESSAGE, PORT)
    server.serve_forever()
```