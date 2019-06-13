from PIL import Image
img = Image.new('RGB', (50, 50))
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
            pixels[i, j] = (round(((i+j)/100)*255), round((i/50)*255), round((j/50)*255))
img.show()
