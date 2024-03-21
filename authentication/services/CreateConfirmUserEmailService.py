from authentication import models
import environ


class CreateConfirmUserEmail:
    def __init__(self, user) -> None:
        self.user = user
        self.set_token()

    def __delete_old_user_token(self):
        models.ConfirmationEmailToken.objects.filter(user=self.user).delete()

    def set_token(self):
        self.__delete_old_user_token()
        confirmation_token = models.ConfirmationEmailToken.objects.create(
            user=self.user,
        )
        confirmation_token.save()
        self._token = confirmation_token

    def get_token(self):
        return self._token

    def get_url(self):
        env = environ.Env()
        return f"{env('FRONT_URL')}/confirm/{self.get_token().token}"
