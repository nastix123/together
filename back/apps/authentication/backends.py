from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(
                models.Q(username=username) |
                models.Q(email=username) |
                models.Q(phone=username)
            )
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None