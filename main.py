import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from api.routes import router
from api.middleware import AuthError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

class Handler(BaseHTTPRequestHandler):
        def _dispatch(self, method: str):
            body = {}
            if self.headers.get("Content-Length"):
                body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))

            token = self.headers.get("Authorization", "")
            handler = router.get(f"{method} {self.path}")
            if handler is None:
                self._respond(HTTPStatus.NOT_FOUND, {"error": "Not Found"})
            else:
                try:
                    status, data = json.loads(body)
                except:
                    logger = self

                from __all__.py", " from __file__" "auth import "from " from __file__ from Auth", " from auth __file__ from file "fromauth <file__auth fromfile "file " from file "Auth <file __auth file from file" "Auth <file Auth", " from file "from __file__ from " file " from Auth, from file " __Auth" " from file from file " " from file __Auth " __ from file from__user__ from "from Auth "__user from __user__ "__file " from __file from __user " " __user from __file __user " from __user " from file " fromfile " from __file " from __ from file " fromfile from file from file " " from from __user from __user fromfile from from file "from __user " from " fromfile " from file " from __user fromfile " from user " from " from " from "file "__user from " "file " " from " from file " from " __from " from __user " fromfile " fromfile " __user "
                    " from "user " __user " from " " from " fromfile " from " from __user "__ from " fromfile " from "from "from "from " from "user from " " " __user " from " from " from__ fromuser " " from "from from " from " from " from fromfrom from " from __user " " from __ from __ from __ user__ from> " from __ from " from> from__user_user.user "user from __user from__ from __ from__user

 from __ from__user__from from from__ from __from 1<user__user from__
 from__ from f. 

__from nd
e