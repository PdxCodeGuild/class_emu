# filename: lab16_v1_image_manipulation.py
'''
Lab 16: Image Manipulation

Let's convert an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'.

> First download the file from here and place it in the same directory as your code
> (or save it anywhere and use an absolute path when opening it).
> If you don't have pillow installed, run pip install pillow in a terminal.
> You can check if pillow using pip show pillow.

Use the formula for converting to greyscale and the code below.
Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math will often use floats.
'Y' is used to represent the brightness. The following formula get the brightness of an RGB triplet.
To convert to greyscale, set R, G, and B to Y.

Y = 0.299*R + 0.587*G + 0.114*B

##### Sample Code #####

from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here

        pixels[i, j] = (r, g, b)

img.show()
'''

from PIL import Image
img = Image.open("lab16_images/rgb_color_wheel.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        Y = round((.3*r + .6*g + .1*b)) # Al's code
        pixels[i, j] = (Y, Y, Y)        # Al's code
img.show()
