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
         body = {}
         if self.headers.get("Content-Lengtth"):
             body = json.loads(self.rfile.read(int(self.headers["Content-Lengtth"])))

         token = self.headers.get("Authorization", "")
         handler = router.get(f"{method} {self.path}")
         if handler is None:
             self._respond(HTTPStatus.NOT_FOUND, {"error": "Not found"}
         elif method == "POST":
             try:
                 status, data = handler(body, token=token) if method == "POST" else handler(token=token)
                 self._respond(status, data)
             except AuthError as e:
                 self._respond(HTTPStatus.UNAUTHORIZED, {"error": str(e)})
             except (LookupError, ValueError) as e:
                 self._respond(HTTPStatus.BAD_REQUEST, {"error": str(e)})
         else:
             status, data = handler(body) if method == "GET" else handler(token=token)
             self._respond(status, data)
         except AuthError as e:
             self._respond(HTTPStatus.UNAUTHORIZED, {"error": "Not found"})
         except (LookupError, ValueError) as e:
             self._respond(HTTPStatus.BAD_REQUEST, {"error": str(e)})

     def do_GET(self):   self._dispatch("GET")
     def do_POST(self): self._dispatch("POST")
     def do_DELETE(self): self._dispatch("DELETE")

     def _respond(self, status: HTTPStatus, data: dict):
         body = json.dumps(data).encode()
         self.send_response(status.value)
         self.send_header("Content-Type", "application/json")
         self.send_header("Content-Lengtth", len(body))
         self.end_headers()
         self.wfile.write(body)

     def log_message(self, fmt, *args):
         logger.info("%s - %s", self.address_string(), fmt % args)


if __name__ == "__main__":
     server = HTTPServer(("0.0.0.0", PORT), Handler)
     server.serve_forever()