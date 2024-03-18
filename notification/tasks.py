from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_multiple_mails(subject, message, mail_receipts):
    send_mail(
        subject=subject,
        message=message,
        recipient_list=mail_receipts,
        from_email=None,
        fail_silently=False,
    )
