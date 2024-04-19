import environ
from django.template.loader import render_to_string
from notification import tasks


class SendMailService:
    def __init__(self, subject, template, list_receipts_mail, variables) -> None:
        self.subject = subject
        self.template = template
        self._list_receipts_mail = self.set_list_receipts_mail(list_receipts_mail)
        self.variables = variables

    def set_list_receipts_mail(self, mails):
        return mails if isinstance(mails, list) else [mails]

    def __get_html_content(self):
        return render_to_string(
            self.template,
            self.variables,
        )

    def send_mails(self):
        env = environ.Env()

        if env.bool("SEND_MAIL_PROD"):
            tasks.send_multiple_mails.delay(
                self.subject,
                self.__get_html_content(),
                self._list_receipts_mail,
            )

        else:
            tasks.send_mail_test.delay(
                subject=self.subject,
                html_content=self.__get_html_content(),
                mail_receipts=self._list_receipts_mail,
            )
