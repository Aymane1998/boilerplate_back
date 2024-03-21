from notification import tasks


class SendMailService:
    def __init__(self, subject, message, list_receipts_mail) -> None:
        self.subject = subject
        self.message = message
        self._list_receipts_mail = self.set_list_receipts_mail(list_receipts_mail)

    def set_list_receipts_mail(self, mails):
        return mails if isinstance(mails, list) else [mails]

    def send_mails(self):
        tasks.send_multiple_mails(self.subject, self.message, self._list_receipts_mail)
