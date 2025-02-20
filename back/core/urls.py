from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from apps.authentication.views import CreateTokenView, RefreshTokenView, VerifyTokenView, RegistrationViewSet
from core.conf import settings
from core.env import env

urlpatterns = [
    path("api/v1/", include("api.v1")),
    path("admin/", admin.site.urls),
    path("jwt/create/", CreateTokenView.as_view(), name="jwt-create"),
    path("jwt/refresh/", RefreshTokenView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", VerifyTokenView.as_view(), name="jwt-verify"),
    path(
        "auth/register/",
        RegistrationViewSet.as_view({"post": "create"}),
        name="register",
    ),
]

if env.bool("DJANGO_ENABLE_SWAGGER", default=False):
    # SWAGGER
    urlpatterns += [
        # YOUR PATTERNS
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        # Optional UI:
        path(
            "docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
        path(
            "api/schema/redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
