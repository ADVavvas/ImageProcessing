#Vaporwave aesthetic generator 
from PIL import Image, ImageFilter
img = Image.open("image.jpg")

redChannel = img.copy()
blueChannel = img.copy()

redChannel[:,:,0] = 0
blueChannel[0,:,:] = 0


redChannel.show()



