from django.db import models
from django.utils.translation import gettext_lazy as _


class UserPermissions(models.TextChoices):
    view_user = "view_user", _("Can view User list")
    create_user = "create_user", _("Can add User")
    change_user = "change_user", _("Can change User")
    delete_user = "delete_user", _("Can delete User")
    reset_password = "reset-password", _("Can reset password")


class PermissionsForPermissions(models.TextChoices):
    add_permission = "add_permission", _("Can add permission")
    change_permission = "change_permission", _("Can change permission")
    delete_permission = "delete_permission", _("Can delete permission")
    view_permission = "view_permission", _("Can view permission")


class GroupPermissions(models.TextChoices):
    add_group = "add_group", _("Can add group")
    change_group = "change_group", _("Can change group")
    delete_group = "delete_group", _("Can delete group")
    view_group = "view_group", _("Can view group")
    set_users = "set_users", _("Can set users")
    get_group_users = "get_group_users", _("Can get group users")
    get_only_group = "get_only_group", _("Can get only group")
