from django.contrib.auth.models import Permission
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        if user.is_superuser and user.is_active:
            permissions = list(Permission.objects.values_list("codename", flat=True))
        else:
            permissions = list(
                user.user_permissions.filter(user=user).values_list(
                    "codename",
                    flat=True,
                )
            )
        token["permissions"] = permissions

        return token
