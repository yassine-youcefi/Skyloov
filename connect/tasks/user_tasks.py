from celery import shared_task
from connect.mails import MailUtil
from django.contrib.auth.models import User

  
@shared_task
def add(user_id):
    print('instance ',user_id)
    user = User.objects.get(id=user_id)
    send_mail = MailUtil(user, str(user.email))
    send_mail.send_email_welcome()