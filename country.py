class Country():
	def __init__(self, name, currency):
		self.name = name
		self.currency = currency
		
class Countries():
	def __init__(self):
		self.list_of_countries = []
		
	def create_and_add_country(self, name, currency):
		new_country = Country(name, currency)
		self.list_of_countries.append(new_country)
	
	def add_country(self, country):
		self.list_of_countries.append(country)
	
	def __str__(self):
		result = "Countries Currency:"
		for c in self.list_of_countries:
			result += "\n" + c.name + " " + c.currency
		return result
	
