from authentication import models

from django.db.models import Q


class CheckCreationUser:
    def __init__(self, email) -> None:
        self.email = email
        self.valid_domains = []

        self._set_user()

    def get_username_user(self):
        return self.email.split("@")[0]

    def _set_user(self):
        query_users = models.User.objects.filter(
            Q(email=self.email) | Q(username=self.get_username_user())
        )
        if query_users.exists():
            self._user = query_users.first()
        else:
            self._user = None

    def get_user(self):
        return self._user

    def check_user_exist(self):
        return self.get_user()

    def check_email_valid_domaine(self):
        if len(self.valid_domains) == 0:
            return True

        for domain in self.valid_domains:
            if domain in self.email:
                return True

        return False

    def check_user_active(self):
        if self.check_user_exist():
            return self.get_user().is_active

        return False
