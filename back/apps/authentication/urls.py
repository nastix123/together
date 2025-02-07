from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RequestViewSet, ResponseViewSet
from .views import UserRegistrationView

router = DefaultRouter()
router.register('requests', RequestViewSet)
router.register('responses', ResponseViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
]