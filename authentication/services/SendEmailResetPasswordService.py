from authentication import models

import environ

from notification import services


class SendMailResetPasswordService:
    def __init__(self, user) -> None:
        self.user = user
        self.template = "../../notification/templates/reset_password_template.html"

    def __get_url_reset_password(self):
        env = environ.Env()

        token = models.TokenResetPassword.objects.create(
            user=self.user,
        )
        url_front = env("FRONT_URL")
        url = f"{url_front}/reset/{token.token}"

        return url

    def __get_variables(self):
        variables = {"url_reset_password": self.__get_url_reset_password()}

        return variables

    def handler(self) -> None:
        subject = "Changement de mot de passe portail préstataire"

        service_send_email = services.SendMailService(
            subject=subject,
            template=self.template,
            list_receipts_mail=self.user.email,
            variables=self.__get_variables(),
        )
        service_send_email.send_mails()
