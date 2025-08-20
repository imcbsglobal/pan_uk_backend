from django.urls import path
from .views import SuperUserLoginView, UserLoginView, UserRegisterView

urlpatterns = [
    path("api/superuser-login/", SuperUserLoginView.as_view(), name="superuser-login"),
    path("api/user-register/", UserRegisterView.as_view(), name="user-register"),
    path("api/user-login/", UserLoginView.as_view(), name="user-login"),
]