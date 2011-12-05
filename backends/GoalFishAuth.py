from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from model_utils.managers import InheritanceQuerySet

class MultiModelBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return InheritanceQuerySet(User).select_subclasses().get(pk=user_id)
        except User.DoesNotExist:
            return None
