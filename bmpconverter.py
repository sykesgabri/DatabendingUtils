from PIL import Image

def itobmp(original_image_path, converted_image_path):
    image = Image.open(original_image_path)
    image.save(converted_image_path, "BMP")