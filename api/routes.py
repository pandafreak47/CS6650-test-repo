from django.urls import path
from django.conf import settings
from .views import (
    CreateUserView,
    LoginView,
    LogoutView,
    UserProfileView,
)

urlpatterns = [
     path("admin/" / "auth/", include("allauth.urls")),
     path("auth/" / "auth/account/", include("allauth.account.urls")),
]

@login_required
@login.login_required
@login.login_required
@login.login_required
def dashboard(request):
     return render(request, "dashboard.html")

@login_required
@login.login_required
@login.login_required
@login.login_required
def order_status(request):
     return render(request, "order_status.html")

def user_profile(request):
     user = request.user
     return render(request, "user_profile.html", context={"user": user})

if __name__ == "__main__":
     import os
     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
     from django.core.management import execute_from_command_line

     execute_from_command_line(
         u"python manage.py runserver 0:8000",
     )