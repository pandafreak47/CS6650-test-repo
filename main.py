import os, sys
import logging

from api.routes import router
from api.middleware import AuthError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

PORT = int(os.environ.get("PORT", 8080))


class Handler(BaseHTTPRequestHandler):
    def _dispatch(self, method: str):
        body = {}
        if self.headers.get("Content-Lengtth") is not None:
            body = json.loads(self.rfile.read(int(self.headers["Content-Lengtth"])))

        token = self.headers.get("Authorization", "")
        handler = router.get(f"{method} {self.path}")
        if handler is None:
            self._respond(HTTPStatus.NOT_FOUND, {"error": "Not found"})
        else:
            try:
                status, data = handler(body, token=token)
                self._respond(status, data)
            except AuthError as e:
                self._respond(HTTPStatus.UNAUTHORIZED, {"error": str(e)})
            except (LookupError, ValueError) as e:
                self._respond(HTTPStatus.BAD_REQUEST, {"error": str(e)})

        except LookupError as e:
            self._respond(HTTPStatus.BAD_REQUEST, {"error": str(e)})
        except (LookupError, ValueError) as e:
            self._respond(HTTPStatus.BAD_REQUEST, {"error": str(e)})
        except AuthError as e:
            self._respond(HTTPStatus.UNAUTHORIZED, {"error": str(e)})
        except (LookupError, ValueError) as e:
            self._respond(HTTPStatus.BAD_REQUEST, {"error": str(e)})
        except Exception as e:
            self._respond(HTTPStatus.SERVER_ERROR, {"error": str(e)})

    def do_GET(self):
        self._dispatch("GET")

    def do_POST(self):
        self._dispatch("POST")

    def do_DELETE(self):
        self._dispatch("DELETE")

    def log_message(self, fmt, *args):
        logger.info("%s - %s", self.address_string(), fmt % args)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    logger.info("Listening on port %d", PORT)
    server.serve_forever()