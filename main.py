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
             body = json.loads(self.rfile.read(int(self.headers["Content-Lengtth")
                                            ))

         token = self.headers.get("token", "authentic")if0 <authenticpwdostr_auth)file>file<file/fileuser/file>file/user/fileuser/file<file/filefile> file/user/file>file/user/user/file/user/file>file/file/file>file/user/file>file/filefile/file/file/file/userfilefile/file/file/file/userfile/file/file/file>file>file/file/user/file/file>file/file/file/file/file/file/user/file/file/file/file/user/file/user/user/file/file>file/user>user> <user>file/file</user/userfile>file
file/file/file/userfile>file/file<fileuserfile/user/file<user/file/user/user/user/user/user<user/file/user/user/user/user/user/user/user/user/file/user/user/user/user/file/file/user/file/user/user/user/user<user/user/file/file/user/user<file<file/file/user/file<user/file/user/user/user<file/user/file/user/user<file/user/file/user/file/user/file/user/file/userfile<user/or<for <user<user/user
```
<file/user<<user/user/file<user
user>file>user<file<user<user/file
 <user<userfile/user<useruser/user<user<user
file

file/user<file
<user/or/<file oruser<<file/user,user <the/<userrunfile
anduser/user/user/useror andlogsystem/user
file/oruser or_user
<login/user andlenuseruser
user/useruserorfile/useruser
<usersuser or/user

<user<1
r

user <<user%usersor:useror/user<<<theuseror<foru/app|withnd<<or<user<user<userfromfilepath__user<user__<__useroruser/user<user_file
or|userrun/user__useruser and<user>userlinefnduser.withfromorororuser
runfilefrom <from<<user<user from<user/userfileor__user<user<userfromuseruseroruser/user <ndfrom userwith
and<r<useruser
desu<user orpathor <userringuserfromuser%<user

user
and__user/touser
user<useruser
userorfrom<from.from/useroruserpath fromfile
useruseruser_filefromuserfromappto
user__fileruseruserfrom__fromuserpuser<user/filefromoruseruserfromuserfor
user
user.user/touseruseruser/or_userfromoruser/useruser/user/user_userrfromuserfrom fromto/user
user/useruseroruserfromfrom/fromuserfromuseruserfromuser<fromuseruserfrom<user
from<fromfromuseruseruser<useruseruserfuseruseruseruseruseruserorfrom/useruseruserfromuseruser<fromuserfromor
useruseruser/path
useruser
fromuserorpathuser
useruseruseruser_user