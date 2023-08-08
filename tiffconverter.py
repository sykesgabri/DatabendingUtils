from PIL import Image
import os

def itotiff(original_image_path, converted_image_path):
    image = Image.open(original_image_path)
    image.save(converted_image_path, format="TIFF", compression=None)
    os.system('tiffcp -p separate converted_image.tiff converted_image_rrggbb.tiff')
    os.remove(converted_image_path)
    os.rename('converted_image_rrggbb.tiff', 'converted_image.tiff')
