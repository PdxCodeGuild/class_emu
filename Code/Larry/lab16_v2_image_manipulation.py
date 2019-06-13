# filename: lab16_v2_image_manipulation.py
'''
Lab 16: Image Manipulation

Version 2
Use the colorsys library to increase the saturation, decrease the saturation, and rotate the hue.
Colorsys represents colors as floats in the range 0.0 - 1.0, whereas pillow uses ints in the range 0 - 255.
You'll have to convert between these two representations.

##### Sample code #####
import colorsys
# colorsys uses colors in the range [0, 1]
h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

# do some math on h, s, v

r, g, b = colorsys.hsv_to_rgb(h, s, v)

# convert back to [0, 255]

r = int(r*255)
g = int(g*255)
b = int(b*255)
'''

import colorsys
from PIL import Image
# img = Image.open("lab16_images/gradient_orig.png") # must be in same folder -- this image has 3 channels - rgb
img = Image.open("lab16_images/gradient.png") # must be in same folder -- this image has 4 channels - rgba

width, height = img.size
pixels = img.load()

which_conversion = input('''How do you want to manipulate the image?
Type (ch) to change the hue
Type (ls) to decrease the saturation
Type (hs) to increase the saturation
Type (lv) to decrease the value
Type (hv) to increase the value
> ''')

for i in range(width):
    for j in range(height):
        # print(pixels[i, j])
        if len(pixels[0, 0]) == 4:          # runs when img = lab16_images/gradient.png (rgba)
            r, g, b, a = pixels[i, j]
        else:                               # runs when img = lab16_images/gradient_orig.png (rgb)
            r, g, b = pixels[i, j]
        # Y = round((.3*r + .6*g + .1*b)) # Al's code, this is for converting to grayscale
        # pixels[i, j] = (Y, Y, Y)        # Al's code, this is for converting to grayscale

        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        # do some math on h, s, v
        if which_conversion == 'ch':
            h = h / 2
        elif which_conversion == 'ls':
            s = s * .3
        elif which_conversion == 'hs':
            s = s * 3
        elif which_conversion == 'lv':
            v = v * .2
        elif which_conversion == 'hv':
            v = v * 2

        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        # a = 255

        # convert back to [0, 255]
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        if len(pixels[0, 0]) == 4:          # runs when img = lab16_images/gradient.png (rgba)
            pixels[i, j] = (r, g, b, a)
        else:                               # runs when img = lab16_images/gradient_orig.png (rgb)
            pixels[i, j] = (r, g, b)

img.show()
