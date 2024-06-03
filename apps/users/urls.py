from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from apps.users.views import UserCreateViewSet, UserViewSet

app_name = "users"

router = DefaultRouter()
router.register(r"", UserViewSet)
router.register(r"", UserCreateViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
