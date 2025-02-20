from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users.models import Custom_User


class PermissionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        fields = [
            "id",
            "name",
            "codename",
        ]

    def get_name(self, obj):
        return _(obj.name)


class GroupSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True,
    )

    class Meta:
        model = Group
        fields = ["id", "name", "user_set", "permissions"]


class AddUsersToGroupSerializer(serializers.Serializer):
    users = serializers.PrimaryKeyRelatedField(
        queryset=Custom_User.objects.all(),
        many=True,
    )