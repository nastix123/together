from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.db import models


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



class Custom_User(AbstractBaseUser):
    USER_TYPES = (
        ('volunteer', 'Volunteer'),
        ('needy', 'Needy'),
    )
    phone = models.CharField(max_length=15, unique=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    is_active = models.BooleanField(default=True)

    objects = CustomManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username", ]


class RequestModel(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    author = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='requests')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='open')


class ResponseModel(models.Model):
    request = models.ForeignKey(RequestModel, on_delete=models.CASCADE, related_name='responses')
    volunteer = models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='responses')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
