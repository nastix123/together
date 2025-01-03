from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.authentication.permissions import UserPermissions
from core.constants import AbsModel


class CustomManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self._create_user(username, password, **extra_fields)

    def _create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbsModel, AbstractBaseUser, PermissionsMixin):
    """Базовая модель user."""

    first_name = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("first_name"),
    )
    last_name = models.TextField(
        max_length=255, blank=True, null=True, verbose_name=_("last_name")
    )
    middle_name = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("middle_name"),
    )
    username = models.EmailField(
        blank=True,
        null=True,
        unique=True,
        verbose_name=_("email"),
    )
    phone = models.CharField(
        blank=True,
        null=True,
        max_length=20,
        unique=True,
        verbose_name=_("phone"),
    )
    password = models.CharField(max_length=255)
    appointment = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("appointment"),
    )
    job_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("job_title"),
    )

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    objects = CustomManager()
    EMAIL_FIELD = "username"

    def __str__(self):  # noqa ANN204
        return (
            f"{self.first_name}"
            f"{self.last_name}"
            f"{self.middle_name}"
            f"{self.appointment}"
            f"{self.job_title}"
            f"{self.username}"
            f"{self.phone}"
            f"{self.is_active}"
            f"{self.is_staff}"
            f"{self.is_superuser}"
        )

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        default_permissions = []
        permissions = UserPermissions.choices
