from PIL import Image, ImageFilter, ImageChops, ImageShow
import numpy as np
import random

#Need to change some parameters here and there
#Make use of direction

#L: left, R: right, B: both
direction = 'B'
#displacement in percentage
max_displacement = 4
#width in percentage
min_width = 4
max_width = 75
#height in percentage
min_height = 1
max_height = 2
#max number of glitches
max_glitch = 18
#min number of glitches
min_glitch = 12

glitches = random.randint(min_glitch, max_glitch)

img = Image.open("image2.jpg")

data = np.asarray(img)
img_data = data.copy()
dimensions = data.shape

displacement = int(max_displacement * 0.01 * dimensions[0])

for i in range(glitches):
  width = random.randint(min_width, max_width)
  height = random.randint(min_height, max_height)
  height = int(dimensions[1] * height * 0.01)
  width = int(dimensions[0] * width * 0.01)
  y = random.randint(0, dimensions[1] - height - 1) 
  x = random.randint(displacement, dimensions[0] - width - 1)
  for h in range(y, height + y):
    for w in range(x, width + x):
      img_data[h,w - displacement, :] = img_data[h, w, :]

merged = Image.fromarray(img_data)

merged.show()
