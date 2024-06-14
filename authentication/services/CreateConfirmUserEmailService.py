from authentication import models
import environ
from notification import services


class CreateConfirmUserEmail:
    def __init__(self, user, list_receipts_mail) -> None:
        self.user = user
        self.set_token()
        self.subject = "Confirmation de l'adresse mail pour le portail prestataire"
        self.template = "../../notification/templates/creation_user_template.html"
        self.list_receipts_mail = list_receipts_mail

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

    def __get_variables(self):
        return {"url_confirmation_creation_user": self.get_url()}

    def handler(self):
        service = services.SendMailService(
            subject=self.subject,
            template=self.template,
            list_receipts_mail=self.list_receipts_mail,
            variables=self.__get_variables(),
        )
        service.send_mails()
