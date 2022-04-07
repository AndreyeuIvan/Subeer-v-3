from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from . import views as accounts_views


urlpatterns = [
    re_path(r"^signup/$", accounts_views.signup, name="signup"),
    re_path(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    re_path(
        r"^login/$",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
]
