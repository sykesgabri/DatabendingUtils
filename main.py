import colorama
from colorama import Fore, Back, Style

from bmp_mode import bmp_mode
from tiff_mode import tiff_mode

# display ascii art logo
with open('logo.txt', 'r', encoding='utf-8') as file:
    art = file.read()
print(Fore.MAGENTA + art)
print(Style.RESET_ALL + 'Version 1.0')
print("IMPORTANT: This version currently generates corrupted TIFF files instead of usable ones. I'm currently not sure why, but I'll fix it eventually.")
print('For now, use the BMP mode, as that works fine.')

# ask user what mode they wish to use
print('Do you wish to work with TIFF or BMP?')
print("NOTE: Even if you already have an image with either of these formats, this step will ensure that more advanced image properties are properly set up for databending.\n")

print('TIFF = 1')
print('BMP = 2\n')

while True:
    desired_format = input('(1/2): ')

    if desired_format == '1':
        tiff_mode()
        break
    elif desired_format == '2':
        bmp_mode()
        break
    else:
        print('Invalid input. Please try again.')