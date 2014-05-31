class Coin():
	def __init__(self, nominal_value):
		self.nominal_value = nominal_value
		
	@property 
	def nominal(self):
		return self.nominal_value
		
	@nominal.setter
	def nominal(self, value):
		if value > 0:
			self.nominal_value = value