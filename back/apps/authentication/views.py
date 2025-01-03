from djoser.views import UserViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from apps.authentication.models import CustomUser
from apps.authentication.permissions import UserPermissions
from apps.authentication.serializers import (
    UserCreateSerializer,
    UserSerializer,
    UserUpdateSerializer,
)
from core.utils.permissions_utils import CheckPermissions
from core.views import AbsCRUDView


@extend_schema(tags=["auth: user"])
class UserAuthViewSet(AbsCRUDView):
    queryset = CustomUser.objects.prefetch_related(
        "groups",
    )
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    action_serializers = {
        "create": UserCreateSerializer,
        "update": UserUpdateSerializer,
    }

    http_method_names = ["get", "post", "put", "head", "options"]


@extend_schema(tags=["auth: user"])
class CreateTokenView(TokenObtainPairView):
    pass


@extend_schema(tags=["auth: user"])
class RefreshTokenView(TokenRefreshView):
    pass


@extend_schema(tags=["auth: user"])
class VerifyTokenView(TokenVerifyView):
    pass


@extend_schema(tags=["auth: user"])
class DjoserUserViewSet(UserViewSet):
    pass
