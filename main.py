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

PORT = int(os.environ.get("PORT", 8080))


class Handler(BaseHTTPRequestHandler):
    def _dispatch(self, method: str):
        logger.info("Dispatching %s %s", method, self.path)
        body = {}
        if self.headers.get("Content-Length"):
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))

        token = self.headers.get("Authorization", "")
        handler = router.get(f"{method} {self.path}")
        if handler is None:
            self._respond(HTTPStatus.NOT_FOUND, {"error": "Not found"})
            return

        try:
            status, data = handler(body, token=token) if method == "POST" else handler(token=token)
            self._respond(status, data)
        except AuthError as e:
            self._respond(HTTPStatus.UNAUTHORIZED, {"error": str(e)})
        except (LookupError, ValueError) as e:
            self._respond(HTTPStatus.BAD_REQUEST, {"error": str(e)})

    def do_GET(self):
        logger.info("GET request received")
        self._dispatch("GET")

    def do_POST(self):
        logger.info("POST request received")
        self._dispatch("POST")

    def do_DELETE(self):
        logger.info("DELETE request received")
        self._dispatch("DELETE")

    def _respond(self, status: HTTPStatus, data: dict):
        logger.info("Responding with status %d", status.value)
        body = json.dumps(data).encode()
        self.send_response(status.value)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        logger.info("%s - %s", self.address_string(), fmt % args)


if __name__ == "__main__":
    logger.info("Starting Order Management Service")
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    logger.info("Listening on port %d", PORT)
    server.serve_forever()
```