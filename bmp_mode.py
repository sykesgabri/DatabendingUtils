import os

from clear import clear

from bmpconverter import itobmp

from removebmpheader import rmbmph

from returnbmpheader import rtbmph

# define important variables
converted_image_path = 'converted_image.bmp'
headless_converted_image_path = 'headless_converted_image'
raw_headless_converted_image_path = 'headless_converted_image.raw'
databent_output_path = 'databent_output.bmp'

def bmp_mode():
    clear()
    print('You have chosen BMP.')
    print('Type the path of the image you wish to use, it will be converted automatically.\n')
    
    original_image_path = input('Input image path: ')
    print('\n')
    
    print('Using', original_image_path, 'as input image.\n')
    
    print('Converting image to BMP...\n')
    itobmp(original_image_path, converted_image_path)
    
    print('Removing BMP header from image...\n')
    rmbmph(converted_image_path, headless_converted_image_path)
    
    print('Open Audacity. Go to file>import>raw data. Import "headless_converted_image" from the same folder this program is running in.')
    print('Set Encoding to "U-Law", Byte Order to "Little Endian", Channels to "1 Channel (Mono)", and click "Import".')
    print('Proceed to databend your image by adding whatever audio effects you wish.\n')
    
    print('Once you have databent your image, go to file>export>as wav. Under "Save as type" choose "Other uncompressed files", make sure "Header" is set to "RAW (header-less)" and "Encoding" is set to "U-Law". Click "Save".')
    print('IMPORTANT: Do NOT change the file name or extension. Do NOT save anywhere other than the same folder this program is running inside of.\n')
    
    print('Once your databent image has been saved, type the following and hit enter:')
    print('I am ready to get an output image.\n')
    
    while True:
        ready = input()
        
        if ready == 'I am ready to get an output image.':
            print('\n')
        
            print('Generating databent_output.bmp...\n')
            rtbmph(converted_image_path, raw_headless_converted_image_path, databent_output_path)
            
            print('Deleting', converted_image_path,'...\n')
            os.remove(converted_image_path)
            
            print('Deleting', headless_converted_image_path,'...\n')
            os.remove(headless_converted_image_path)
            
            print('Deleting', raw_headless_converted_image_path,'...\n')
            os.remove(raw_headless_converted_image_path)
            
            print('Done. Enjoy your databent image!')
            break
        else:
            print('Invalid input. Please try again.')
    exit()