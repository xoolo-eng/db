from django.urls import path
from django.shortcuts import redirect
from user.views import UsersView, login, RegisterView, logout


urlpatterns = [
    path("users/", UsersView.as_view(), name="all_users"),
    path("login/", login, name="user_login"),
    path("register/", RegisterView.as_view(), name="register_user"),
    path("logout/", logout, name="logout_page"),
    path("", lambda request: redirect("all_users"))
]