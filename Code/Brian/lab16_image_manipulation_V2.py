# lab16_image_manipulation_V2.py
'''
** Version 2 **

Use the colorsys library to increase the saturation, decrease the saturation, and rotate the hue.
Colorsys represents colors as floats in the range 0.0 - 1.0, whereas pillow uses ints in the range 0 - 255.
You'll have to convert between these two representations.

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
import colorsys # imports colorsys
from PIL import Image # imports Image file from PIL
img = Image.open("lenna.png") # must be in same folder
width, height = img.size # gets the image size and assings it to variable width, height
pixels = img.load() # creates the pixels map

for i in range(width): # creates a for loop for i in the range of width
    for j in range(height): # creates a for loop for j in the range of height
        r, g, b = pixels[i, j] # assigns r, g, b to pixels at indecies i, j

        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255) # converts rgb to hsv

        if h < 0.1 or h > 0.8:
            s = 1

        r, g, b = colorsys.hsv_to_rgb(h, s, v) # converts hsv to rgb

        # convert back to [0, 255]
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)

img.show() # shows the image with the modifications in the above code
