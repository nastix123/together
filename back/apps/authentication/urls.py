from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RequestViewSet, ResponseViewSet, UserLoginView
from .views import UserRegistrationView

router = DefaultRouter()
router.register('requests', RequestViewSet)
router.register('responses', ResponseViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view({'post': 'create'}), name='register'),
    path('login/', UserLoginView.as_view({'post': 'create'}), name='login'),
    path('', include(router.urls)),
]