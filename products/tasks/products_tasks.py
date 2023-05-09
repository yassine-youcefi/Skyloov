
import threading
import requests
from celery import shared_task
from connect.mails import MailUtil
from products.models import Products
from products.utils import resize_image
import multiprocessing
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.storage import default_storage
  
 
@shared_task
def product_media_task(product_id):
    product = Products.objects.get(id=product_id)
    image_field = product.image
    image_path = default_storage.path(image_field.name)
    
    # Open the image file using Pillow
    img = Image.open(image_path)
    
    # Generate the thumbnail
    img.thumbnail((200, 200))

    # Save the thumbnail to the product model
    thumb_io = BytesIO()
    img = img.convert('RGB')
    img.save(thumb_io, format='JPEG')
    product.image_thumbnail.save(f'{product.name}_thumb.jpg', File(thumb_io))
    product.save()
    img.close()
        