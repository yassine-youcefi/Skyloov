from PIL import Image

def resize_image(image_file, size):
    print('size',size)
    with Image.open(image_file) as img:
        img = img.resize(size)
        return img
