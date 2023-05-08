
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from connect.tasks import user_tasks



@receiver(post_save, sender=User)
def user_welcome(sender, instance, created, **kwargs):
    '''
        send email welcome 
    '''
    if created:
        user_tasks.add.apply_async(args=[instance.id])
        
