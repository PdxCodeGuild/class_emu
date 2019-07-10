
from PIL import Image, ImageDraw
import random
import math
counter_inside = 0
counter_outside = 0
n_samples = 1000000

width = 10000
height = 10000
img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)
draw.rectangle(((0, 0), (width, height)), fill='white')

for i in range(n_samples):
    px = random.random()
    py = random.random()
    img_x = px * width
    img_y = (1-py) * height
    color = ''
    distance = math.sqrt(px*px + py*py)
    if distance <= 1:
        counter_inside += 1
        color = 'red'
    else:
        counter_outside += 1
        color = 'blue'
    draw.rectangle(((img_x, img_y), (img_x+1, img_y+1)), fill=color)
    if (i%10000 == 0):
        print(f'{round(i/n_samples*100,2)}%')
        pi = counter_inside/(counter_outside + counter_inside)*4
        print(f'{abs(pi-math.pi)/math.pi}%')



# the origin (0, 0) is at the top-left corner




img.show()
