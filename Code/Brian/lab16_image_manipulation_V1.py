# lab16_image_manipulation_V1.py
'''
Lab 16: Image Manipulation

** Version 1 **

Let's convert an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'.
First download the file from here and place it in the same directory as your code (or save it anywhere and use an absolute path when opening it).
If you don't have pillow installed, run pip install pillow in a terminal. You can check if pillow using pip show pillow.

Use the formula for converting to greyscale and the code below.
Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math will often use floats.
'Y' is used to represent the brightness. The following formula get the brightness of an RGB triplet.
To convert to greyscale, set R, G, and B to Y.

Y = 0.299*R + 0.587*G + 0.114*B

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

from PIL import Image # imports Image file from PIL
img = Image.open("lenna.png") # must be in same folder
width, height = img.size # gets the image size and assings it to variable width, height
pixels = img.load() # creates the pixels map

for i in range(width): # creates a for loop for i in the range of width
    for j in range(height): # creates a for loop for j in the range of height
        r, g, b = pixels[i, j] # assigns r, g, b to pixels at indecies i, j
        Y = round(.299*r + .587*g + .114*b) # assigns variable Y to the rounded values by multiplying desired numbers by r, g and b
        pixels[i, j] = (Y, Y, Y) # takes the indicies of pixes and applies Y to each
img.show() # shows the image with the modifications in the above code
