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
 from __all__.py", " from file" "auth import "from " from api.User from __file" fromauth <file__auth fromfile "file " from file "Auth <file __auth file from file" "Auth <file Auth", file __file from fileAuth from __file from __file __ Auth, __ from auth Auth, from file Auth Auth " from file fromfile from __file,Auth from file from Auth, Auth from file, Auth, from__user__ from Auth,Auth fromfile from from /__Auth, Auth from file from __file, Auth from file from __from Auth, from __ fromfile from __file from __file from Auth from Auth from __file from __from Auth from Auth from <from __file from __Auth
from file /Auth
from /Auth from /Auth Authfile
from,Auth from /file fromAuth fromfile, fromAuth from file <from Authfile
from
from file
from file, Auth from file from from file from <from file from from Auth from fileAuth from file from from from file
from fileAuth from fromfile from from fromFile from from file fromAuth from __from <file Auth from Auth
fromAuth file

<fileAuth, file
file ->
 <from fromfile /file>file <from file<from<File
file/file,file <<file /file
file >
file
file /File
<
<
file
file,file,file, file and<<create <session -> ->filefile
api
<user/session
<<users/file <__file <file >api<<
files
files
user
UserAuth <user
files < < < <User
<auth
file -> = <userUser
<<requests
<import ->auth,userapi,file