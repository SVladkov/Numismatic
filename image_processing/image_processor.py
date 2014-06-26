from PIL import ImageFilter
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps

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
				
			column -= 2 
		
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
				if pixel_column_difference[k] > 60:
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
					
			column += 2
			
	def find_upper_border(self):
		row = 1
		column = 0
		
		pixel_row_difference = []
		number_of_consecutive = 0
		in_sequence = False
		sequence_start = 0
		has_big_difference = False
		
		while row < self.height:
			pixel_row_difference = self.find_row_difference(row, -1)
			for k in range(len(pixel_row_difference)):
				if pixel_row_difference[k] > 60:
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
					sequence_start = row
			else:
				in_sequence = False
				number_of_consecutive = 0
				
			row += 2
		
	def find_lower_border(self):
		row = self.height - 2
		column = 0
		
		pixel_row_difference = []
		number_of_consecutive = 0
		in_sequence = False
		sequence_start = 0
		has_big_difference = False
		
		while row > 0:
			pixel_row_difference = self.find_row_difference(row, 1)
			for k in range(len(pixel_row_difference)):
				if pixel_row_difference[k] > 40:
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
					sequence_start = row
			else:
				in_sequence = False
				number_of_consecutive = 0
				
			row -= 2
		
	def find_row_difference(self, row, row_compare):
		counter = 0
		pixel_row_difference = []
		
		while counter < self.width:
			red_difference = self.pixels[counter, row][0] - self.pixels[counter, row + row_compare][0]
			green_difference = self.pixels[counter, row][1] - self.pixels[counter, row + row_compare][1]
			blue_difference = self.pixels[counter, row][2] - self.pixels[counter, row + row_compare][2]
			
			red_difference = abs(red_difference)
			green_difference = abs(green_difference)
			blue_difference = abs(blue_difference)
			
			pixel_row_difference.append(red_difference + green_difference + blue_difference)
			counter += 2	
			
		return pixel_row_difference
			
	def find_column_difference(self, column, column_compare):
		counter = 0
		pixel_column_difference = []
		
		while counter < self.height:
			red_difference = self.pixels[column, counter][0] - self.pixels[column + column_compare, counter][0]
			green_difference = self.pixels[column, counter][1] - self.pixels[column + column_compare, counter][1]
			blue_difference = self.pixels[column, counter][2] - self.pixels[column + column_compare, counter][2]
			
			red_difference = abs(red_difference)
			green_difference = abs(green_difference)
			blue_difference = abs(blue_difference)
			
			pixel_column_difference.append(red_difference + green_difference + blue_difference)
			counter += 2	
			
		return pixel_column_difference
		
	def make_coin_image(self):
		self.crop()
		cropped_coin = self.cropped
		cropped_coin.convert('RGBA')
			
		pixels_of_cropped = cropped_coin.load()
		middle_x = (self.right - self.left) / 2
		middle_y = (self.lower - self.upper) / 2
		radius = middle_x - 1
		
		#ImageProcessor.draw_circle(pixels_of_cropped, middle_x, middle_y, radius)
		
		self.make_background_transparent(cropped_coin)
		
		cropped_coin.save("cropped_coin.png")
		
	def crop(self):
		self.left = self.find_left_border()
		self.right = self.find_right_border()
		self.upper = self.find_upper_border()
		self.lower = self.find_lower_border()
		
		box = (self.left, self.upper, self.right, self.lower)
		self.cropped = self.image.crop(box)		
		
	@staticmethod
	def draw_circle(pixels, center_x, center_y, radius):
		x = radius
		y = 0
		radius_error = 1 - x
		
		while x >= y - 1:
			pixels[center_x + x, center_y + y] = (0, 0, 0, 100)
			pixels[center_x + y, center_y + x] = (0, 0, 0, 100)
			pixels[center_x - x, center_y + y] = (0, 0, 0, 100)
			pixels[center_x - y, center_y + x] = (0, 0, 0, 100)
			pixels[center_x - x, center_y - y] = (0, 0, 0, 100)
			pixels[center_x - y, center_y - x] = (0, 0, 0, 100)
			pixels[center_x + x, center_y - y] = (0, 0, 0, 100)
			pixels[center_x + y, center_y - x] = (0, 0, 0, 100)
			
			y += 1
			
			if radius_error < 0:
				radius_error += 2 * y + 1
			else:
				x -= 1
				radius_error += 2 * (y - x + 1)
			
	def make_background_transparent(self, cropped_coin):
		'''transparent_area = (10,20,30,40)
		mask=Image.new('L', self.image.size, color=255)
		draw=ImageDraw.Draw(mask) 
		draw.rectangle(transparent_area, fill=0)
		self.image.putalpha(mask)
		self.image.save('output.png')
		'''
		
		size = (self.right - self.left, self.right - self.left)
		mask = Image.new('L', size, 0)
		draw = ImageDraw.Draw(mask) 
		draw.ellipse((0, 0) + size, fill=255)
		output = ImageOps.fit(cropped_coin, mask.size, centering=(0.5, 0.5))
		output.putalpha(mask)
		output.save('output.png')
			
	def find_edges(self):
		self.edge_image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
		self.edge_image.show()
			
			
			
			
			
			
			
			
			