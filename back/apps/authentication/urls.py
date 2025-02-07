from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.authentication.views import RequestViewSet, ResponseViewSet, UserRegistrationView, UserLoginView

router = DefaultRouter()
router.register('requests', RequestViewSet)
router.register('responses', ResponseViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view({'post': 'create'}), name='register'),
    path('login/', UserLoginView.as_view({'post': 'create'}), name='login'),
    path('', include(router.urls)),
]