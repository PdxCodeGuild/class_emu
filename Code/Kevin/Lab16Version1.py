from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here
        y = 0.299*r + 0.587*g + 0.114*b
        
        y = int(y)
        r, g, b = y, y, y
        pixels[i, j] = (r, g, b)

img.show()