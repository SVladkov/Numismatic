class Coin():
	def __init__(self, nominal_value):
		self.nominal_value = nominal_value
		
	@property 
	def Nominal(self):
		return self.nominal_value
		
	@Nominal.setter
	def Nominal(self, value):
		if value > 0:
			self.nominal_value = value