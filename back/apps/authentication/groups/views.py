from django.contrib.auth.models import Group, Permission
from drf_spectacular.utils import extend_schema
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from shop_project.mixins import SerializerActionMixin
from users.groups.serializers import PermissionSerializer, GroupSerializer, AddUsersToGroupSerializer
from users.permissions import PermissionsForPermissions, GroupPermissions
from users.serializers import UserSerializer
from users.utils import PermissionActionMixin, CheckPermissions


@extend_schema(tags=["roles: permissions"])
class PermissionViewSet(
    SerializerActionMixin, PermissionActionMixin, ListModelMixin, GenericViewSet
):
    def_code = [
        "view_session",
        "delete_session",
        "change_session",
        "add_session",
        "view_contenttype",
        "delete_contenttype",
        "change_contenttype",
        "add_contenttype",
        "view_logentry",
        "delete_logentry",
        "change_logentry",
        "add_logentry",
        "add_profile",
        "change_profile",
        "delete_profile",
        "view_profile",
        "view_tokenproxy",
        "add_tokenproxy",
        "change_tokenproxy",
        "delete_tokenproxy",
        "add_token",
        "change_token",
        "delete_token",
        "view_token",
    ]
    queryset = Permission.objects.exclude(codename__in=def_code).prefetch_related(
        "user_set"
    )
    serializer_class = PermissionSerializer
    permission_by_action = {
        "list": (CheckPermissions(PermissionsForPermissions.view_permission),)
    }
    search_fields = ["name", "name_ru", "codename"]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ("id",)
    ordering = ("-id",)


@extend_schema(tags=["roles: groups"])
class GroupViewSet(
    PermissionActionMixin,
    ModelViewSet,
):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_by_action = {
        "list": (CheckPermissions(GroupPermissions.view_group),),
        "create": (CheckPermissions(GroupPermissions.add_group),),
        "put": (CheckPermissions(GroupPermissions.change_group),),
        "patch": (CheckPermissions(GroupPermissions.change_group),),
        "delete": (CheckPermissions(GroupPermissions.delete_group),),
    }

    @action(
        detail=True,
        methods=["post"],
        serializer_class=AddUsersToGroupSerializer,
        url_path="set-users",
    )
    def set_users(self, request, pk=None):
        group = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = serializer.validated_data.get("users", [])
        group.user_set.set(users)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=["GET"], url_path="get-users")
    def get_group_users(self, request, pk=None):
        group = self.get_object()
        users = group.user_set.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)