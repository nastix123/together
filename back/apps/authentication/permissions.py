from rest_framework.permissions import BasePermission
from apps.authentication.backends import CustomAuthBackend

class IsNeedy(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'needy'

class IsVolunteer(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'volunteer'

d = CustomAuthBackend()