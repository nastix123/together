from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.authentication import views
from apps.authentication.views import RequestViewSet, ResponseViewSet, Custom_UserViewSet

router = DefaultRouter()
router.register('requests', RequestViewSet)
router.register('responses', ResponseViewSet)
router.register(r'users', Custom_UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
