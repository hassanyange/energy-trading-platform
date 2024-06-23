from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            users = UserModel.objects.filter(email=username)
        except UserModel.DoesNotExist:
            # If no user with the given email exists, return None
            return None
        else:
            # Check each user found with the given email
            for user in users:
                if user.check_password(password):
                    return user
        return None