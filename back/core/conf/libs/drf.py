REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
}

DRF_STANDARDIZED_ERRORS = {
    "EXCEPTION_FORMATTER_CLASS": "core.utils.exception_formatter.MyExceptionFormatter",  # noqa E501
    "ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True,
    "NESTED_FIELD_SEPARATOR": ".",
    "ALLOWED_ERROR_STATUS_CODES": [
        "400",
        "401",
        "403",
        "404",
        "405",
        "406",
        "415",
        "429",
        "500",
    ],
    "ERROR_SCHEMAS": None,
    "LIST_INDEX_IN_API_SCHEMA": "INDEX",
    "DICT_KEY_IN_API_SCHEMA": "KEY",
    "ERROR_COMPONENT_NAME_SUFFIX": "ErrorComponent",
}
