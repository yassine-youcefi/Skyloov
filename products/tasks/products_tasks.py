
import requests
import threading
import multiprocessing
from celery import shared_task
from connect.mails import MailUtil
from products.models import Products
from products.utils import generate_thumbnail

from django.core.files import File
from django.core.files.storage import default_storage


@shared_task
def product_media_task(product_id):
    product = Products.objects.get(id=product_id)
    image_field = product.image
    image_path = default_storage.path(image_field.name)
    size = (200, 200)
    thumbnail = generate_thumbnail(image_path, size)
    product.image_thumbnail.save(f'{product.name}_thumb.jpg', File(thumbnail))
    product.save()
