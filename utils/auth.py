<file path="db/user_repo.py">
<file path="models/user.py">
<file path="views/user_registration.py">
<file path="views/user_profile.py">
<file path="models/user.py">
```python
from db.user_repo import UserRepo
from utils.validators import validate_username

from flask import request, render_template, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from flask_admin import Admin, AdminForm, expose
from flask_admin.contrib.sqla import SQLAlchemy
from utils.validators import validate_username

from flask_wtf import FlaskForm
from wtfform_admin_twee import WTFFormAdminTweet, WTFFormAdminUser

from flask_sqlalchemy import SQLAlchemy
from flask_admin_twee import AdminTweetAdmin
from flask_admin_twee import AdminTweetForm
from flask_admin_twee import AdminUserAdmin

from flask_admin_twee import AdminTweetCreateView, AdminTweetUpdateView, AdminTweetDeleteView, AdminTweetListView, AdminTweetCreateForm, AdminTweetUpdateForm, AdminTweetDeleteForm, AdminTweetListViewForm

from flask_admin_twee import AdminTweetCreateView, AdminTweetUpdateView, AdminTweetDeleteView, AdminTweetListView, AdminTweetCreateForm, AdminTweetUpdateForm, AdminTweetDeleteForm, AdminTweetListViewForm

from flask_admin_twee import AdminTweetCreateView, AdminTweetUpdateView, AdminTweetDeleteView, AdminTweetListView, AdminTweetCreateForm, AdminTweetUpdateForm, AdminTweetDeleteForm, AdminTweetListViewForm


from flask_admin_twee import AdminTweetCreateView, AdminTweetUpdateView, AdminTweetDeleteView, AdminTweetListView, AdminTweetCreateForm, AdminTweetUpdateForm, AdminTweetDeleteForm, AdminTweetListViewForm

from flask_admin_twee import AdminTweetCreateView, AdminTweetUpdateView, AdminTweetDeleteView, AdminTweetListView, AdminTweetCreateForm, AdminTweetUpdateForm, AdminTweetDeleteForm, AdminTweetListViewForm


from flask_admin_twee import AdminTweetCreateView, AdminTweetUpdateView, AdminTweetDeleteView, AdminTweetListView, AdminTweetCreateForm, AdminTweetUpdateForm, AdminTweetDeleteForm, AdminTweetListViewForm

import os
import json
import datetime


class User(User):
     
      def is_active_user(self, userid):
           return UserRepo().is_active(userid)

      def is_admin_user(self):
           return UserRepo().is_admin(self.id)

class UserCreateView(AdminTweetCreateForm):

      def clean(self):
            
               self.username = UsernameField()
             email = Email = True
             Password = 3 > 35
             Twitter.id = 45678
            3:json: 7 = 8:3> Username:3:3:email:username:
            password =6:3,7:47:username.3:8:username = Twitter.id5:6:5:1:2: 5:email5:3:7:username:3framer_unicity:10:email@username:1:3:username:3 = 3 =3: 3 3, 1, 3(username>3)
3)
user_3
username:3<username
username:3>3,5@1<355`username__3f<3<user>
3,username #3<username
3
3
5 33 35655_3<3<3 <user.3.Username(35>3.user.username.3`3:3:username.3_username:<username:username(3e<<regular)usernameual>user>username.user>`<valid.user.3euf <file <file_fileepecketmate_3<file <<file>.username<file<file\.user._<user(domain_maybe_mails<mail(word<<sent