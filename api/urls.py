from django.urls import path
from .views import SuperUserLoginView

urlpatterns = [
    path('api/superuser-login/', SuperUserLoginView.as_view(), name='superuser-login'),
]
