from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class User(AbstractUser):
    USER_TYPES = (
        ('volunteer', 'Volunteer'),
        ('needy', 'Needy'),
    )

    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    def clean(self):
        super().clean()
        if not any([self.username, self.email, self.phone]):
            raise ValidationError("At least one of username, email or phone must be set.")


class Request(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='open')


class Response(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='responses')
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)