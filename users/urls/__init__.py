from django.urls import path

from users.views.auth import LogoutView, UserLoginView
from users.views.user import UserProfileView

app_name = "users"

urlpatterns = [
    path("", UserProfileView.as_view(), name="index"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
