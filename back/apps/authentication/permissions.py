from rest_framework.permissions import BasePermission

class IsNeedy(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'needy'

class IsVolunteer(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'volunteer'