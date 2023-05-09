from PIL import Image
from io import BytesIO


def generate_thumbnail(image_path, size):
    print('size', size)
    # Open the image file using Pillow
    img = Image.open(image_path)

    # Generate the thumbnail
    img.thumbnail((200, 200))

    # Save the thumbnail to the product model
    thumb_io = BytesIO()
    img = img.convert('RGB')
    img.save(thumb_io, format='JPEG')
    return thumb_io
