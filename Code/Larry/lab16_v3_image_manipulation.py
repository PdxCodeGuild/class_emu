# filename: lab16_v3_image_manipulation.py

from PIL import Image, ImageDraw

width = 450
height = 450
fill_color = (128, 128, 128)  # grey
outline_color = (0, 0, 0) # darkgrey

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

# paint the background white
draw.rectangle(((0, 0), (width, height)), fill="white")

#helper
# draw.ellipse((left, top, right, bottom), outline={color}, fill={color})
# draw.line((topX, topY, bottomX, bottomY), outline={color}, fill={color})

# head
draw.ellipse((155, 5, 295, 145), fill=fill_color)

# body
draw.line((225, 140, 225, 300), width=50, fill=fill_color)

# left arm
draw.line((225, 220, 125, 175), width=50, fill=fill_color)

# right arm
draw.line((225, 220, 325, 175), width=50, fill=fill_color)

# left leg
draw.line((225, 300, 150, 425), width=50, fill=fill_color)

# right leg
draw.line((225, 300, 300, 425), width=50, fill=fill_color)

# show the image
img.show()
