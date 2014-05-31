import unittest

import country

class CountryTest(unittest.TestCase):	
	def test_country_creation(self):
		Bulgaria = country.Country("Bulgaria", "Levas")
		self.assertEqual(Bulgaria.name, "Bulgaria")
		self.assertEqual(Bulgaria.currency, "Levas")
	
class CountriesTest(unittest.TestCase):
	def test_countries_list_creation(self):
		countries = country.Countries()
	
	def test_addition_of_coutry(self):
		countries = country.Countries()
		Bulgaria = country.Country("Bulgaria", "Levas")		
		countries. add_country(Bulgaria)
		self.assertEqual(str(countries), "Bulgaria Levas\n")
		
	def test_creation_and_addition_of_country(self):
		countries = country.Countries()
		Bulgaria = country.Country("Bulgaria", "Levas")		
		countries.add_country(Bulgaria)
		countries.create_and_add_country("England", "Pound")
		all_countries = "Bulgaria Levas\nEngland Pound\n"
		self.assertEqual(str(countries), all_countries)
		
		
if __name__ == '__main__':
    unittest.main()