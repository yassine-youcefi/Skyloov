from PIL import Image
from io import BytesIO


def generate_thumbnail(image_path):
    """
        This funtion generate image thumbnail with (200, 200) size
    """
    size = (200, 200)
    img = Image.open(image_path)
    img.thumbnail(size)
    thumb_io = BytesIO()
    img = img.convert('RGB')
    img.save(thumb_io, format='JPEG')
    return thumb_io
