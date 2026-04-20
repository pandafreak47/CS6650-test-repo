```
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
              self._respond(HTTPStatus.NOT_FOUND, {"error": "Not found"}())
          else:
              try:
                 status, data = handler(body, token=token)
                 self._respond(status, data)
              except AuthError as e:
                 self._respond(HTTPStatus.UNAUTHORIZED, {"error": "Not found"}())
              except (LookupError, ValueError) as e:
                 self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
              except (LookupError, ValueError) as e:
                 self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
          except AuthError as e:
              self._respond(HTTPStatus.UNAUTHORIZED, {"error": "Bad request"})
          except (LookupError, ValueError) as e:
              self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
          except (LookupError, ValueError) as e:
              self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
          except AuthError as e:
              self._respond(HTTPStatus.UNAUTHORIZED, {"error": "Bad request"})
          except (LookupError, ValueError) as e:
              self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
          except (LookupError, ValueError) as e:
              self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
          except AuthError as e:
              self._respond(HTTPStatus.UNAUTHORIZED, {"error": "Bad request"})
          except (LookupError, ValueError) as e:
              self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
          except (LookupError, ValueError) as e:
              self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
          except AuthError as e:
              self._respond(HTTPStatus.UNAUTHORIZED, {"error": "Bad request"})
          except (LookupError, ValueError) as e:
              self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
          except (LookupError, ValueError) as e:
              self._respond(HTTPStatus.BAAD_REQUEST, {"error": "Bad request"})
          except AuthError as e:
              self._respond(HTTPStatus.UNAUTHORIZED, {"error": "Invalid token"})
              self.response_body = self.render_template('index.html', {
                      "method": "GET", "username": username, "username": username,
                      ous:"value", **{} and not "Bearem.
                      Authenti: verifypassword")
          
app/username: verify("Beare") and "Authentications" username:verify "Bearem")
username "authentication"
username>
<Beauth "Be authentic" _dispatcher
username/rops"
username "username> "BeAuth

username/authentic/authentic "Beauthentics/authentic/authentic "Beauthentic/authentic
```
from_username>
Beific
authentic):
Beaming/
Be <username/authenticific
Be_authenticific):
Beific/authentic
username>username_authentic/authentic/BeBe
authentic
Beific
be /Beific
/Beific
Beific>Be