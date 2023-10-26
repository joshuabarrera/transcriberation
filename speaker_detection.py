import json
import sys

import smartcrop
from PIL import Image

image = Image.open("image.png")
cropper = smartcrop.SmartCrop()
result = cropper.crop(image, 100, 100)
print(json.dumps(result, indent=2))