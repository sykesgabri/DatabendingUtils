from PIL import Image

def itotiff(original_image_path, converted_image_path):
    image = Image.open(original_image_path)
    image.convert("RGB")
    image.save(converted_image_path, "TIFF")