from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated & request.user.is_superuser


class SetPasswordPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated | request.user.is_password_temporary


class CheckPermissions(BasePermission):
    def __init__(self, permissions: object) -> object:
        super().__init__()
        self.permissions = permissions

    def __call__(self):
        return self

    def has_permission(self, request, view):
        return request.user.has_perm(perm=f"apps.{self.permissions.value}")
