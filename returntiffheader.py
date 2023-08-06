def rttiffh(converted_image_path, raw_headless_converted_image_path, databent_output_path):
    with open(converted_image_path, 'rb') as input_file:
        header_data = input_file.read(8)

    with open(raw_headless_converted_image_path, 'rb') as raw_file:
        data = raw_file.read()
        
    with open(databent_output_path, 'ab') as output_file:
        output_file.write(header_data)