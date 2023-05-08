from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .mails import MailUtil



@receiver(post_save, sender=User)
def user_welcome(sender, instance, created, **kwargs):
    '''
        send email welcome 
    '''
    if created:
        send_mail = MailUtil(instance, str(instance.email))
        send_mail.send_email_welcome()
