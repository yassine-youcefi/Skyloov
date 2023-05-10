
import requests
from celery import shared_task
from connect.mails import MailUtil
from products.models import Products
from products.utils import generate_thumbnail
from django.core.files import File
from django.core.files.storage import default_storage


@shared_task
def product_media_task(product_id):
    product = Products.objects.get(id=product_id)
    image_name = product.image.name.split('/')[1].split('.')[0]
    image_path = default_storage.path(product.image.name)
    thumbnail = generate_thumbnail(image_path)
    product.image_thumbnail.save(f'{image_name}_thumb.jpg', File(thumbnail))
    product.save()
