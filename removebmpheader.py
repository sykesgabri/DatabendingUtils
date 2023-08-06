def rmbmph(converted_image_path, headless_converted_image_path):
    with open(converted_image_path, 'rb') as input_file:
        # Skip the 54-byte BMP header
        input_file.seek(54)
        data = input_file.read()

    with open(headless_converted_image_path, 'wb') as output_file:
        output_file.write(data)