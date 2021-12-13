# imageRotate.py
# Minimal example of rotating an image by 90 degrees

from PIL import Image
img = Image.open('./20200912_12251-cropped6.jpg')
img.rotate(90).show()