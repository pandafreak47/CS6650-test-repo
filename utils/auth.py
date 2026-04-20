```

```
from flask import Flask, request, render_template, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, login_required, user_loader
from datetime import datetime

from .connection import get_connection
from .models import User

app = Flask(__name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        user = User(**data)
        db = get_connection()
        db.add(user)
        db.commit()
        return jsonify({'status': 'registered'})
    except Exception as e:
        app.logger.exception(e)
        return jsonify({'status': 'failed', 'error': 'failed to register: {}'.format(e) })

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        email = data['email']
        hashed_password = generate_password_hash(data['password'], method='bcrypt')
        user = User(email=email, hashed_password=hashed_password)
        db = get_connection()
        db.add(user)
        db.commit()
        return jsonify({'status': 'login'})
    except Exception as e:
        app.logger.exception(e)
        return jsonify({'status': 'failed', 'error': 'failed to login: {}'.format(e) })

@login_manager.unload_user
def load_user(user_id):
    return True


@app.route('/logout')
def logout():
    logout_user()
    return jsonify({'status': 'loggedout'})


@app.errorhandler(Exception)
def error(e):
    return make_response('error')


@app.route('/')
def root:user = True
@app.route
```

```