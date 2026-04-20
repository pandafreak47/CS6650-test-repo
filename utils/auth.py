```python
from db.user_repo import UserRepo
from utils.validators import validate_username

from flask import request, render_template, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import UUIDType

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_wtf.csrf import CSRFProtection
from flask_admin import Admin, AdminForm, expose

from flask_admin_tweets import TweetAdmin
from flask_admin_tweets import TweetForm
from flask_admin_tweets.fields import TweetField

from flask_admin_tweets.views import TweetsView

from flask_admin_tweets.models import Tweets
from flask_admin_tweets.models.fields import UserField
from flask_admin_tweets.models.fields import TweetField
from flask_admin_tweets.models.fields import TweetFormField
from flask_admin_tweets.models.fields import TweetLinkField
from flask_admin_tweets.models.fields import TweetLinkListField

from flask_admin_tweets.views import TweetsView

from flask_admin_tweets.admin import AdminTweetsAdmin

from flask_admin_tweets import AdminTweetsAdmin

from flask_admin_tweets.views import TweetCreateView
from flask_admin_tweets.views import TweetUpdateView
from flask_admin_tweets.views import TweetDeleteView

from flask_admin_tweets.views import TweetListView

from flask_admin_tweets.fields import TweetField
from flask_admin_tweets.fields import TweetLinkField
from flask_admin_tweets.fields import TweetLinkListField

from flask_admin_tweets.fields import TweetImageField
from flask_admin_tweets.fields import TweetLinkImageField

from flask_admin_tweets.fields import TweetTagField
from flask_admin_tweets.fields import TweetTagImageField

from flask_admin_tweets.forms import TweetCreateForm
from flask_admin_tweets.forms import TweetUpdateForm
from flask_admin_tweets.forms import TweetDeleteForm

from flask_admin_tweets.forms import TweetListViewForm

import os
import json
import datetime


@login_manager
class User(User):
     
     def is_active_user(self, userid):
         return UserRepo().is_active(userid)

     def is_admin(self, userid):
          return UserRepo().is_admin(userid)

     
     def __repr__(self):
          return "<{}>".format(self.username)

     def __repr__(self):
         
     def __repr__ = self
         
         return User.username.lower()


class UserCreateView:
         UserRepo

         self:

class Tweet:json
username
class: Tweet
class.txt)
username: Tweet:json

self:
class:user

tweet:
Tweet.json

username:json
User
from
username
username:json: Tweet:json
T
username
T

json

json:username


T
T
T

username,json:



T
json:T
T

Tjson

T

T
T
json
json
json
T
T

json
T

T
json
T
json
T
json
json
T
username
user

TT
T
T
json
T

T
T
T,T
T <row
T
T
T
T
json
T, TT
json:username
T
TT
T
T
Tries
TT
Treekries
TT
T files
T
TionsrTtries
withtriesy
TTyringtries for TT