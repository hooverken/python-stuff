# imageRotate.py
# Minimal example of rotating an image retrieved from a URL by 90 degrees

from PIL import Image
from requests import get
import tempfile

tf = tempfile.NamedTemporaryFile(delete=False)
URL = "https://github.com/hooverken/python-stuff/raw/main/20200912_12251-cropped6.jpg"

response = get(URL)
tf.write(response.content)
print(tf.name)
Image.open(tf.name).rotate(90).show()