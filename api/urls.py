# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SuperUserLoginView, UserLoginView, UserRegisterView

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('api/superuser-login/', SuperUserLoginView.as_view(), name='superuser-login'),
    path('api/user-register/', UserRegisterView.as_view(), name='user-register'),
    path('api/user-login/', UserLoginView.as_view(), name='user-login'),
    path('api/', include(router.urls)),
]
