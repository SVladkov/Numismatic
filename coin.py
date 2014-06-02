import country

class Coin():
	def __init__(self, nominal, country, year):
		self._nominal = nominal
		self._country = country
		self._year = year
		
	@property 
	def nominal(self):
		return self._nominal
		
	@nominal.setter
	def nominal(self, value):
		if value > 0:
			self._nominal = value