from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from core.conf import settings
from core.env import env

urlpatterns = [
    path("api/v1/", include("api.v1")),
    path("admin/", admin.site.urls),
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
