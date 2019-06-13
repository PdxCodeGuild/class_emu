# my_pillow.py

from PIL import Image
img = Image.open("rainbow.jpeg")
width, height = img.size
pixels = img.load()
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        if r == g == b:
            pixels[i, j] = (255, 255, 255)
        elif max(r, g, b) == r:
            pixels[i, j] = (255, 0, 0)
        elif max(g, b) == g:
            pixels[i, j] = (0, 255, 0)
        elif max(r, g, b) == b:
            pixels[i, j] = (0, 0, 255)
img.show()
