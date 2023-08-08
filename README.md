# DatabendingUtils

This program converts most images into a format ready for databending. You can choose between BMP or TIFF, which both have different and unique properties when databending.

## Dependencies
To run this program, you need to have the following dependencies installed:
- Python (version 3.0 or higher)
- colorama
- LibTIFF

You can install colorama by running the following command:

`pip install colorama`

As for LibTIFF, it depends on your OS:

<details>
    <summary>Windows</summary>
    <br>
    <ul>
        <li>Download tiff-3.8.2-1.exe from <a href="https://sourceforge.net/projects/gnuwin32/files/tiff/3.8.2-1/">here</a>.</li>
        <li>Run the executable and follow the install process.</li>
        <li>Once the install is finished, open File Explorer, right click "This PC", and click "Properties".</li>
        <li>At the left side of the window that just opened, click "Advanced system settings".</li>
        <li>Click "Environment Variables".</li>
        <li>Under "System variables", click the variable named "Path", then click the "Edit" button.</li>
        <li>Click "New".</li>
        <li>Paste the following directory into the text field and click "OK": <code>C:\Program Files (x86)\GnuWin32\bin</code>.</li>
        <li>Exit out of all the menus you just opened.</li>
    </ul>
</details>
<br>
<details>
    <summary>MacOS</summary>
    <br>
    <ul>
        <li>Download Brew from <a href="https://brew.sh/">here</a>.</li>
        <li>Open a terminal and type <code>brew install libtiff</code></li>
    </ul>
</details>
<br>
<details>
    <summary>Linux</summary>
    <br>
    <ul>
        <li>In Ubuntu and its derivatives, open a terminal and run <code>sudo apt install libtiff-tools</code>.</li>
        <li>In Arch and its derivatives, open a terminal and run <code>sudo pacman -S libtiff</code>.</li>
        <li>For any other package manager, you'll have to look into it yourself, just make sure you end up with a version that supports the <code>tiffcp</code> command.</li>
    </ul>
</details>

## Running the Program
1. Clone this git repository, either with `git clone https://github.com/sykesgabri/DatabendingUtils` or by downloading as a zip.
2. Ensure that you have the required dependencies properly installed.
3. Open a command prompt or terminal and navigate to the DatabendingUtils folder.
4. Run the program with `python3 main.py`

## Databending Tutorial
For a detailed tutorial on how to perform databending with audacity, which this program instructs you to use, you can refer to the following YouTube video:
- [Glitch Photography: The Ultimate Tutorial to Databending Photos with Audacity](https://www.youtube.com/watch?v=Z_Rut5gjwfE)

This tutorial covers the steps for applying effects to image data, important considerations while databending, and additional tips to help you get started with databending photographs.

## License
This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license. You can find more information about the license [here](https://creativecommons.org/licenses/by-nc-sa/4.0/).
