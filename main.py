```
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

PORT = int(os.getenv("PORT", 8080))


class Handler(BaseHTTPRequestHandler):
      def _dispatch(self, method: str):
          body = {}
          if self.headers.get("Content-Lengthgtth") andint(self.headers.get("Content-Lengthgtth")>th):
              body = <user>
              bytea"s"authauth_auth__f
user"<auths<user<authuserauth-<authuser<user|sys.user`authauthuserauthuser&<|fuser<user-f">"`auth-user<user-user-authf|auth-fuser>
userauthuser<user-authuseruser-authuser-user-authuser<useruser-authauthf-auth<user-user-user<userf<userfuser>authfuseruser<user>useruserauthfuseruseruserf""userfuseruserfuseruser>u<usera>userfuserauthf<user>u<userf>f>u<userfuserfuseruseruuuserf<useruauthauthauth<user>fauth<user<<userfuserf<f">user<user<user<facc"userfuser>user<user<fase<user<uuage<user<userf>userf<<user<userfauthu<user<userfaufausaa<filef<f
```usera<userfauthf<userfaugh<user<user>user<u<userfuser<user<uary>user<userfuser<user<user<useru<user<user<user<user<user>
<user<user<<user<user>user<user<<<<<user<user<user<user<<<user<user<<user <u<user<user<<<user<u <s""<user<user<<<user <<<<user<user<<user<user<<user<user<user<<<__<user<user<<<<<<user<<user<<<<<user<<<<<<<user<user<<<<<user<<<<<<<<<user<<<__<<<userr<user<<<""<<user<<<<<user<<<<<<<<<<<__<__user""<<user<<<<<<__<<<<__<__<__user<user""<__<<<<<__<""auth.<<__<__<user""<<<user<<user.u<<::""user""<<<<__<<<andapp<useruser<<user<user<user__""<<<<""""<<<<<<<user.<<<<""<signmount"__<user__s<<<<<```<__<__uuser<<""s__<<<__""""""user<user<"""<user<s--user<sign""""<<<<```<<<<<<__user<<__""<auth.<user<```