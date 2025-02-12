from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.authentication.views import RequestViewSet, ResponseViewSet, UserRegistrationView, UserLoginView, \
    UserLogoutView

router = DefaultRouter()
router.register('requests', RequestViewSet)
router.register('responses', ResponseViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view({'post': 'create'}), name='register'),
    path('login/', UserLoginView.as_view({'post': 'create'}), name='login'),
    path('logout/', UserLogoutView.as_view({'post': 'logout'}), name='logout'),
    path('', include(router.urls)),
]