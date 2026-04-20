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

PORT = int(os.environ.get("PORT", 8080))


class Handler(BaseHTTPRequestHandler):
     def _dispatch(self, method: str):
         body = {}
         if self.headers.get("Content-Lengtth"):
             body = json.loads(self.rfile.read(int(self.headers["Content-Lengtth"]))
         token = self.headers.get("Authorization", "")
         handler = router.get(method="".lower(), f"{self.headers["Authorization"]
         if "GET", "POST", "PUT,POST", f"DELETE")
         token,user "token", "user"
         if "routes")
         body: "fails"
         class "user"
         import "GET "f" "post"
         post, "post "
         token, "POST"
         token "POST" f"GET "POST"
        post/routes "POST" "POST"
POST/POST
POST "POST> POST, _POST"
POST/POST
POST /post

POST "f>posts/POST>user>f>fst>user,POST>s>POST
POSTSPOST,fories
POST, POST
POST
ST, POSTSPOSTSOTS <POSTS <S <SPOST, STOR
STS <Sot >POSTSROS
SPOST
POST
POSTS
POSTS
POSTSOTSPOST,POST =POSTS #POSTSROSSSTS
S

POSTS
<files
path



s


S
f #STS <file
STS:s file

s
SOTS<file
STS
S:s <file(file(user)files.file
<users,user
router ->
<user
<requests
filters,user,file
<user
<file(suser <user.users <user
user ->user <<user
user <users_users:token <user<users<request
user
user user
<
S
user => <<users_resource<user >userUser <userusersusersuser <user <user/s
<user
useruser
user
user
<users <user
user
users
user
user
<<filter<<<<token
<user
<<user<user
<user =<user_user__user_users<user```filter__<validuser::users(_user_users<user(users<user_user_users._user_userusers_user_user_users.user::users_userusers.forauthuser```<user```user
user
users_users._user
users_user_userauthuserusers
usersfilesusers_users_useruser__withuser_auth_users.user<users <users_user_users_users =users_user<user_users
users_send<user_users<users<router
<user_user_<user_users_user_users