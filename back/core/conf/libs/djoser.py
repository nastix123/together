from datetime import timedelta

from cryptography.hazmat.primitives import serialization

from core.env import env

DOMAIN = env.str("DOMAIN")
SITE_NAME = env.str("SITE_NAME")


DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "password-reset?uid={uid}&jwt={token}",
    "ACTIVATION_URL": "password-create?uid={uid}&jwt={token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SERIALIZERS": {
        "user_create": "apps.authentication.serializers.UserCreateSerializer",
        "current_user": "apps.authentication.serializers.UserMeSerializer",
    },
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=env.int("TIME_ACCESS")),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=env.int("TIME_REFRESH")),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("JWT",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "ALGORITHM": env.str("ALGORITHM"),
    "SIGNING_KEY": serialization.load_pem_private_key(
        bytes(env("SIGNING_KEY").replace("\\n", "\n"), "utf-8"),
        password=None,
    ),
    "VERIFYING_KEY": serialization.load_pem_public_key(
        bytes(env("VERIFY_KEY").replace("\\n", "\n"), "utf-8"),
    ),
}
