from django.contrib import admin
from django.urls import path



from django.urls import re_path
from django.conf.urls import include

# from view import views


try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
from django.contrib import admin
from django.shortcuts import redirect
from django.urls.base import reverse

def home(request):
    """Permit to not get 404 while testing."""
    return redirect(reverse("survey-list"))

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r"^$", home, name="home"),
    url("accounts/", include("django.contrib.auth.urls")),
    url(r"^rosetta/", include("rosetta.urls")),
    url(r"^survey/", include("survey.urls")),
    url(r"^admin/", admin.site.urls),

    # re_path('signup', views.signup),
    # re_path('login', views.login),
    # re_path('test_token', views.test_token),
]
