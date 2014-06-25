from PIL import ImageFilter
from PIL import Image

ext = ".jpg"

class ImageProcessor():
	def __init__(self, fileName):
		self.image = Image.open(fileName)
		self.pixels = self.image.load()
		self.w = self.image.size[0]
		self.h = self.image.size[1]
		
	@property
	def width(self):
		return self.w
		
	@property 
	def height(self):
		return self.h
		
	def pixel(self, x, y):
		return self.pixels[x,y]
		
	def set_pixel(self, x, y, red, green, blue):
		red_condition = red >= 0 and red <=255
		green_condition = green >= 0 and green <= 255
		blue_condition = blue >=0 and blue <= 255
		
		if red_condition and green_condition and blue_condition:	
			self.pixels[x,y] = (red, green, blue)
			
	def show(self):
		self.image.show()
		
	def find_right_border(self):
		column = self.width - 2
		j = 0
		
		pixel_column_difference = []
		number_of_consecutive = 0
		in_sequence = False
		sequence_start = 0
		has_big_difference = False
		
		while column > 0:
			pixel_column_difference = self.find_column_difference(column, 1)
			for k in range(len(pixel_column_difference)):
				if pixel_column_difference[k] > 50:
					has_big_difference = True
					break			
				else:
					has_big_difference = False
			
			if has_big_difference:
				if in_sequence:
					number_of_consecutive += 1
					if number_of_consecutive > 50:
						return sequence_start
				else:
					in_sequence = True
					sequence_start = column
			else:
				in_sequence = False
				number_of_consecutive = 0
				
			column -= 1
		
	def find_left_border(self):
		column = 1
		j = 0
		
		pixel_column_difference = []
		number_of_consecutive = 0
		in_sequence = False
		sequence_start = 0
		has_big_difference = False
		
		while column < self.width:
			pixel_column_difference = self.find_column_difference(column, -1)
			for k in range(len(pixel_column_difference)):
				if pixel_column_difference[k] > 50:
					has_big_difference = True
					break
				else:
					has_big_difference = False
					
			if has_big_difference:
				if in_sequence:
					number_of_consecutive += 1
					if number_of_consecutive > 50:
						return sequence_start
				else:
					in_sequence = True
					sequence_start = column
			else:
				in_sequence = False		
				number_of_consecutive = 0					
					
			column += 1
			
	def find_column_difference(self, column, compare):
		j = 0
		pixel_column_difference = []
		
		while j < self.height:
			red_difference = self.pixels[column, j][0] - self.pixels[column + compare, j][0]
			green_difference = self.pixels[column, j][1] - self.pixels[column + compare, j][1]
			blue_difference = self.pixels[column, j][2] - self.pixels[column + compare, j][2]
			
			red_difference = abs(red_difference)
			green_difference = abs(green_difference)
			blue_difference = abs(blue_difference)
			
			pixel_column_difference.append(red_difference + green_difference + blue_difference)
			j += 2	
			
		return pixel_column_difference
			
	def crop(self):
		left = self.find_left_border()
		right = self.find_right_border()
		coin_width = right - left
		
		box = (left, 0, left + coin_width, self.height)
		region = self.image.crop(box)
			
		return region	
			
			
			
			
			
			