from authentication import models
from django.db.models import Q


class GetUserByUsernameOrEmailService:
    def __init__(self, input):
        self.input = input

    def __find_user(self):
        try:
            return models.User.objects.get(Q(username=self.input) | Q(email=self.input))
        except models.User.DoesNotExist:
            return None

    def handler(self):
        user = self.__find_user()
        return user
