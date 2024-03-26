from authentication import models

from django import shortcuts, utils


class ActivateEmailUser:
    def __init__(self, token_value) -> None:
        self.token_value = token_value
        self.get_token()

    def get_token(self):
        token = shortcuts.get_object_or_404(
            models.ConfirmationEmailToken, token=self.token_value
        )
        self._token = token

    def check_expired_toked(self):
        return utils.timezone.now() > self._token.expiration_date

    def handler(self):
        if self.check_expired_toked():
            return False

        user = self._token.user

        if user.is_active:
            self._token.delete()
            return False

        user.is_active = True
        user.save()

        return True

    def get_user(self):
        return self._token.user
