```
from typing import Optional

from app import models, services
from flask import Flask, jsonify, render_template, request
from werkzeug.exception_handlers import default_exception_handler
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.serving import run_server
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key'

app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        if 'file' not in request.files:
            raise abort(400)
        file = request.files['file']
        file_extension = file.filename.split('.')[-1]
        if file_extension not in [ext for ext in ('htm', 'html')]:
            flash('Please enter a file', 'danger')
            return redirect(url_for('upload_form'))
        fileext = '.' + file_extension
        filename = secure_filename(file.original_name.lower())
        file.2)
        #filename
        now
        iffile(file.extension):
        if:file:file:r_file.ext:
        file:rep_hashhash_repo_hash
        hash_hash
        hash_repo_hash:repo_
file:repo:<userh<user>
_hash_repo
hash
user
file_hash<repos:password<user<user<user>
user:user>
```
```
file:repos>useruser:rfile}
```user)
user```
```
user
user:r_user:user_user<user
user_user, file_user_user
user>r user>user>

user_user>user
user
user_user>user:r>user
user
user>user<user>user<user
user