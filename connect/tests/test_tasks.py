import pytest
from celery import states
from django.core import mail
from connect.tasks import user_tasks
from celery.result import AsyncResult
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_welcome_task_sent_after_one_day(user, celery_session_app):
    '''
       Test user welcome send email task 
       assertion : 
            - Check if the task succeeded
    '''

    # Call the Celery task
    task_result = user_tasks.user_welcome_task.delay(user.id)

    # Wait for the task to complete
    result = AsyncResult(task_result.id, app=celery_session_app)

    # Wait for the task to complete
    if celery_session_app.conf.task_always_eager:
        assert task_result.successful()
    else:
        result = AsyncResult(task_result.id, app=celery_session_app)
        result.wait(timeout=10)
        assert result.status == states.SUCCESS
