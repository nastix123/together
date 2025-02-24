from rest_framework import viewsets, permissions
from django.contrib.auth.hashers import make_password

from rest_framework import mixins
from core.views import AbsCRUDView
from .models import RequestModel, ResponseModel, Custom_User
from .serializers import RequestSerializer, ResponseSerializer, RegistrationUserSerializer, \
    GroupSerializer, CreateUserSerializer
from .permissions import IsNeedy, IsVolunteer
from django.contrib.auth.models import Group
from drf_spectacular.utils import extend_schema

from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from djoser.views import UserViewSet


class RequestViewSet(viewsets.ModelViewSet):
    queryset = RequestModel.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated, IsNeedy]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = ResponseModel.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = [permissions.IsAuthenticated, IsVolunteer]

    def perform_create(self, serializer):
        serializer.save(volunteer=self.request.user)


class RegistrationViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Custom_User.objects.all()
    serializer_class = RegistrationUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data["password"]
        user = self.queryset.create(phone=serializer.validated_data["phone"], password=make_password(password))
        user.is_active = True
        user.save()
        return Response({"status": "user maded"})


class Custom_UserViewSet(AbsCRUDView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Custom_User.objects.prefetch_related("groups")
    serializer_class = CreateUserSerializer
    http_method_names = ["get", "post", "put", "head", "options"]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


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
