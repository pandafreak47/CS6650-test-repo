import json
import logging
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus

from api.routes import router
from api.middleref import AuthError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

PORT = int(sys.argv[1] if len(sys.argv)==2 else 8080)


# Define the file<|system|>
defab_valid_callback_def(valid_callback_def(valid,__valid,file<|user|user|file.py,<|user|file, file|valid|user):valid<valid|file.valid|file.py|user|valid|user|valid|user|valid|file|valid|valid|user|user|valid|user|valid|file__valid|user|user|__valid|valid|user|user|valfilevalid|valid|valid|user|valid|valid|valid|valid|valid|valid|valid|valid|user|valid|user|user|user|valid|valid|user|user|user|user|user|user|user|user|user|user|user|user|user<valid|user|user|user|user|user|user|user|user<user|user|user|user<user|user|user|user|user|user|user|user|user|user|user|user|user|user|user|user|useruserval|user|user|user|user_b<user|user|user|user|user|user|user|user|user|user|user|user|user|user|user_valid|user<user|user|user_user<user|user|user|user|user|user|user|user|user|user|user|user|useruser<user|user|user|user|user|user<file<<<<__user|file<file<file|file,file<file...<<<use <file<file<user<<file>><file<<users<f<file<<<<<file<file,file__file<file<file<<<<file>file<file,file <file<<<file<<<<<<<<file<<file <file<<file<<<<user<<<<<<<<<<file <<file<<<<<file<<<<<file<<<<<file<<<file_<<<<file, <<<<<file<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<file/<<file <__file```<<<file<<<file<<<<<<<<<<<<<<<<<<<<<<<<<valid__<<file <<<file:<<<<<file<__<<b<file<call__call<<<valid__call_<valid.```valid_<<valid
<<file<<<valid<<<<<<<<<<<call__
<valid<and<<valid