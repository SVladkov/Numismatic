from PIL import ImageFilter
from PIL import Image

ext = ".jpg"

class ImageProcessor():
	def __init__(self, fileName):
		self.image = Image.open(fileName)
		self.pixels = self.image.load()
		