from PIL import Image
img_in = Image.open("rainbow.jpeg")
img_out = Image.new('RGB', img_in.size)
pixels_in = img_in.load()
pixels_out = img_out.load()
width, height = img_in.size

for j in range(height-50):
	counter = 0
	for i in range(width-50):
		# i2 = i
		# j2 = (j+50)-(counter%100)
		j2 = j
		i2 = (i+50)-(counter%100)
		pixels_out[i, j] = pixels_in[i2,j2]

		counter = (counter + 2)

img_out.show()


'''
for i in range(width-50):
	for j in range(height-50):
		j2 = j
		i2 = (i+50)-(counter%100)
		i2 = i
		j2 = (j+50)-(counter%100)
		pixels_out[i, j] = pixels_in[i2,j2]

		counter = (counter + 2)
'''
