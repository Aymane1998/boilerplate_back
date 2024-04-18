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
        # try:
        return render_to_string(
            self.template,
            self.variables,
        )

    # except:
    #     if isinstance(self.template, str):
    #         return self.template

    #     else:
    #         raise ValueError("template variable doesn't have good type.")

    def send_mails(self):
        tasks.send_multiple_mails.delay(
            self.subject, self.__get_html_content(), self._list_receipts_mail
        )
