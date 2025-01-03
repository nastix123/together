from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.authentication.groups.views import GroupViewSet, PermissionViewSet
from apps.authentication.views import (
    CreateTokenView,
    DjoserUserViewSet,
    RefreshTokenView,
    UserAuthViewSet,
    VerifyTokenView,
)

router = SimpleRouter()
router.register("users", UserAuthViewSet)
router.register("permissions", PermissionViewSet)
router.register("groups", GroupViewSet)

urlpatterns = [
    path("jwt/create/", CreateTokenView.as_view(), name="jwt-create"),
    path("jwt/refresh/", RefreshTokenView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", VerifyTokenView.as_view(), name="jwt-verify"),
    path(
        "reset-password-confirm/",
        DjoserUserViewSet.as_view(
            {"post": "reset_password_confirm"}, name="reset-password-confirm"
        ),
    ),
    path(
        "user-create/",
        DjoserUserViewSet.as_view({"post": "create"}, name="user-create"),
    ),
    path("me/", DjoserUserViewSet.as_view({"get": "me"}), name="me"),
    path("update-me/", DjoserUserViewSet.as_view({"put": "me"}), name="update_me"),
    path(
        "change-password/",
        DjoserUserViewSet.as_view({"post": "set_password"}),
        name="user-change-password",
    ),
    *router.urls,
]
