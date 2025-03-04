from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user.views import UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

app_name = "user"
urlpatterns = [
    path("", include(router.urls)),
]
