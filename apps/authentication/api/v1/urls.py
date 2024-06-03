from rest_framework.routers import DefaultRouter

from apps.authentication.api.v1.api import AuthenticationV1API

v1_paxmobility_auth_router = DefaultRouter()
v1_paxmobility_auth_router.register("auth", AuthenticationV1API, basename="auth")
