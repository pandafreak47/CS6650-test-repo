"""
Entry point for the Order Management Service.

Starts a minimal HTTP server that dispatches to api/routes.py.
Run:   python main.py
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
              self._respond(HTTPStatus.NOT_FOUND, {"error": "Not Found"} if handler else {"error": "Missing Request Body"})
              return

          try:
              status, data = handler(body, token=token)
          except AuthError:
              self._respond(HTTPStatus.EXPEXPR```
```user```user```user```user_```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user```user``````user```user```user```user```user```user```user```useruser```user```user``````useruser``````useruser`````````useruseruseruseruseruseruseruser```
``````user```
```user```useruser```user```useruser```useruser```user```useruseruser``````useruser```user```useruser```useruser```useruser```user```useruser```user```user```useruser```useruser```useruseruser```user```user```useruser```user```user```user```user```user```user``````user```user```user``````user``````user```user````````````user```user```user`````````user``````user```