from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
    )
from django.urls import path, re_path, include
from users import views
from versions.v1.router import api_urlpatterns as api_v1
from versions.v2.router import api_urlpatterns as api_v2

router = routers.DefaultRouter()

urlpatterns = [
    re_path(r'^api/v1/', include(api_v1)),
    re_path(r'^api/v2/', include(api_v2)),
    path('api/payment/users/', include("users.urls")),
    path("api/payment/signup/", views.SignUpView.as_view(), name="signup"),
    path("api/payment/login/", views.LoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("api/payment/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/payment/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
urlpatterns += router.urls

# {
#     "message": "Logeado correctamente",
#     "email": "admin@mail.com",
#     "tokens": {
#         "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxNTEyMzQwLCJpYXQiOjE2NzE1MTE0MzQsImp0aSI6IjJkY2M1OGVlMmNhNDQxMmU5MzMxOTc5NTkyMjA5NDVjIiwidXNlcl9pZCI6MX0.Ii08f6bvE6p5z42ycw7WJZ7zJawKiLWgQPSmYw46KCM",
#         "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MTU5NzgzNCwiaWF0IjoxNjcxNTExNDM0LCJqdGkiOiJiOWFjNzQwNjU4ZDI0ZjJhYTQ2Mjk2NmMzYjJlYjMyOSIsInVzZXJfaWQiOjF9.kixjMO65NdQSiJlFnDXkz0BqMFSe56k_EoTKzanpfwU"
#     }
# }

# {
#     "message": "Logeado correctamente",
#     "email": "david@mail.com",
#     "tokens": {
#         "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxMzEzMzU0LCJpYXQiOjE2NzEzMTMwNTQsImp0aSI6IjQyYTJmNGQ0MmQzNjRlM2VhZmUxYTIyYTUwYTIwMzBkIiwidXNlcl9pZCI6Mn0.gaTHKPvFTVzKa6AXcKqHja74Npu4vhT9fWzwhwidD4g",
#         "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MTM5OTQ1NCwiaWF0IjoxNjcxMzEzMDU0LCJqdGkiOiI3YjIzMTUxNjUzN2Y0MjlhODk0MDU0ODQyZDU0OTY2ZCIsInVzZXJfaWQiOjJ9.KM2fNc5UozNIYEQxyG1wA-q04WXTBSYhUml93pDo_jw"
#     }
# }