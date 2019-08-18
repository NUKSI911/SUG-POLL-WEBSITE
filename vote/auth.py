""" Custom Authentication backends """

from django.contrib.auth.backends import ModelBackend
from vote.models import User


class AuthenticationMatricNumberAnyNameBackend():
    """ Allow authentication with emails """

    def authenticate(self, request, username=None, password=None, **kwargs):
        """ confirm validity of information """

        try:
            user = User.objects.get(matric_number__iexact=username)
        except User.DoesNotExist:
            return None
        else:
            if password.lower() in [x.lower() for x in (user.first_name,\
                    user.last_name, user.middle_name) if x]:
                return user
        return None

    def get_user(self, user_id):
        """ get user object """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
