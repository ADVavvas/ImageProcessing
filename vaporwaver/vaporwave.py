#Vaporwave aesthetic generator 
from PIL import Image, ImageFilter, ImageChops, ImageShow
import numpy as np

shift = 'R'
blur = False
shift_amount = 10
shift_amount *= -1

img = Image.open("image.jpg")

data = np.asarray(img)

red_chnl = data[:,:,0]
blue_chnl = data[:,:,2]
green_chnl = data[:,:,1]

"""
#Get color channels as images:

placeholder = np.zeros(data.shape)

red_img = placeholder.copy()
red_img[:,:,0] = red_chnl
red = Image.fromarray(red_img.astype('uint8'))

blue_img = placeholder.copy()
blue_img[:,:,2] = blue_chnl
blue = Image.fromarray(blue_img.astype('uint8'))

red = ImageChops.offset(red, 1, 0)
blue = ImageChops.offset(blue, -1, 0)
"""
red_chnl = Image.fromarray(red_chnl)
blue_chnl = Image.fromarray(blue_chnl)
green_chnl = Image.fromarray(green_chnl)

if shift == 'R':
  red_chnl = ImageChops.offset(red_chnl, shift_amount, 0)
  if blur:
    red_chnl = red_chnl.filter(ImageFilter.GaussianBlur(2))
elif shift == 'G':
  green_chnl = ImageChops.offset(green_chnl, shift_amount, 0)
  if blur:
    green_chnl = green_chnl.filter(ImageFilter.GaussianBlur(2))
elif shift == 'B':
  blue_chnl = ImageChops.offset(blue_chnl, shift_amount, 0)
  if blur:
    blue_chnl = blue_chnl.filter(ImageFilter.GaussianBlur(2))
else:
  print('Color shift can only be on R, G or B.')


merged = Image.merge('RGB', (red_chnl, green_chnl, blue_chnl))

merged.show()

