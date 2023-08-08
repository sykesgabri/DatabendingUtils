import os

from clear import clear

from tiffconverter import itotiff

#from removetiffheader import rmtiffh

#from returntiffheader import rttiffh

# define important variables
converted_image_path = 'converted_image.tiff'
headless_converted_image_path = 'headless_converted_image'
raw_headless_converted_image_path = 'headless_converted_image.raw'
databent_output_path = 'databent_output.tiff'

def tiff_mode():
    clear()
    print('You have chosen TIFF.')
    print('Type the path of the image you wish to use, it will be converted automatically.\n')

    original_image_path = input('Input image path: ')
    print('\n')

    print('Using', original_image_path, 'as input image.\n')

    print('Converting image to TIFF and setting pixel order to per channel...\n')
    itotiff(original_image_path, converted_image_path)

    '''
    print('Removing TIFF header from image...\n')
    rmtiffh(converted_image_path, headless_converted_image_path)
    '''

    print('Open Audacity. Go to file>import>raw data. Import "converted_image.tiff" from the same folder this program is running in.')
    print('Set Encoding to "U-Law", Byte Order to "Little Endian", Channels to "1 Channel (Mono)", and click "Import".')
    print('Proceed to databend your image by adding whatever audio effects you wish.')
    print('IMPORTANT: TIFF Mode does not currently remove the header and IFD from TIFF images. Refer to README.md to avoid corrupting this data.\n')

    print('Once you have databent your image, go to file>export>as wav. Under "Save as type" choose "Other uncompressed files", make sure "Header" is set to "RAW (header-less)" and "Encoding" is set to "U-Law". Click "Save".')
    print('After you have saved "converted_image.raw", you can change the file extension to TIFF and view it as a normal TIFF image.\n')

    '''
    print('Once your databent image has been saved, type the following and hit enter:')
    print('I am ready to get an output image.\n')

    while True:
        ready = input()

        if ready == 'I am ready to get an output image.':
            print('\n')

            print('Generating databent_output.tiff...\n')
            rttiffh(converted_image_path, headless_converted_image_path, databent_output_path)

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
    '''
    exit()
