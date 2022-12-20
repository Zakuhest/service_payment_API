from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
    )
from django.urls import path, re_path, include
from users import views
from versions.v1.router import api_urlpatterns as api_v1
from versions.v2.router import api_urlpatterns as api_v2

router = routers.DefaultRouter()

urlpatterns = [
    path("api/payment/signup/", views.SignUpView.as_view(), name="signup"),
    path("api/payment/login/", views.LoginView.as_view(), name="login"),
    path("api/payment/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/payment/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path('api/payment/users/', include("users.urls")),
    re_path(r'^api/v1/', include(api_v1)),
    re_path(r'^api/v2/', include(api_v2)),
]
urlpatterns += router.urls