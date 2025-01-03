from rest_framework import serializers

from apps.authentication.groups.serializers import GroupSerializer
from apps.authentication.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "username",
            "is_active",
            "phone",
            "appointment",
            "job_title",
            "groups",
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "username",
            "is_active",
            "phone",
            "appointment",
            "job_title",
            "groups",
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        read_only_fields = ("id",)
        fields = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "username",
            "is_active",
            "phone",
            "appointment",
            "job_title",
        )


class UserMeSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        read_only_fields = (
            "id",
            "phone",
            "appointment",
            "job_title",
        )

        fields = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "phone",
            "appointment",
            "job_title",
            "groups",
            "permissions",
        )

    def get_permissions(self, obj):
        return [perm.split(".")[1] for perm in obj.get_group_permissions()]
