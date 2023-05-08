import pytest
from celery import Celery
from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


@pytest.fixture(scope='session')
def celery_session_app(request):
    app = Celery('myapp',
                 broker=settings.REDIS_URL,
                 backend=settings.CELERY_RESULT_BACKEND)

    # Establish a new connection for each test
    app.conf.task_always_eager = True
    app.conf.task_eager_propagates = True

    return app


@pytest.fixture
def user():
    registration_date = timezone.now() - timedelta(minutes=5)
    user = User.objects.create(username='testuser', password='testpassword')
    return user
