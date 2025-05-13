# If you want to use SAML to log users into Admin site automatically, you've got to use this.
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class SamlUserAuth(BaseBackend):
    def get_user(self, userId):
        try:
            return User.objects.get(pk=userId) # you MUST use pk for this method or else it will not work properly
        except User.DoesNotExist:
            return None

    def authenticate(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        userId = user.pk
        return self.get_user(userId=userId)
