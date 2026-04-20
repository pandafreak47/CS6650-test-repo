<task>
Add type annotations to all function signature.
</task>

<file>
from django.urls import path
from django.conf import settings
from .views import (
    CreateUserView,
    LoginView,
    LogoutView,
    UserProfileView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("allauth.urls")),
    path("auth/", include("allauth.account.urls")),
]

from django.contrib.auth.decorators import login_required
from django.views.generic import (
    login,
    registration,
    login_required,
)

@login_required
@login.login_required
@login_required
@login.login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
@login.login_required
@login.login_required
@login.login_required
def order_status(request):
    return render(request, "order_status.html")

from . import views

if __name__ == "__main__":
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(
        u"python manage.py runserver 0:8000",
    )