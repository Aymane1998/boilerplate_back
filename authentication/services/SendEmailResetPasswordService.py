from authentication import models

import environ

from notification import services


class SendMailResetPasswordService:
    def __init__(self, user) -> None:
        self.user = user

    def __get_url_reset_password(self):
        env = environ.Env()

        token = models.TokenResetPassword.objects.create(
            user=self.user,
        )
        url_front = env("FRONT_URL")
        url = f"{url_front}/reset/{token.token}"

        return url

    def __get_message(self):
        message = f"""
            Voici le lien pour changer de mot de passe {self.__get_url_reset_password()}.

            Si vous n'êtes pas à l'origine de cette demande vous pouvez ignorer ce message.
        """
        return message

    def handler(self) -> None:
        subject = "Changement de mot de passe portail préstataire"
        message = self.__get_message()

        service_send_email = services.SendMailService(
            subject=subject,
            message=message,
            list_receipts_mail=self.user.email,
        )
        service_send_email.send_mails()
