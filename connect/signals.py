
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from connect.tasks import user_tasks
from datetime import timedelta
from django.utils import timezone



@receiver(post_save, sender=User)
def user_welcome(sender, instance, created, **kwargs):
    '''
        send email welcome 
    '''
    if created:
        eta = instance.date_joined + timedelta(days=1)
        user_tasks.user_welcome_task.apply_async(args=[instance.id], eta=eta)
        
