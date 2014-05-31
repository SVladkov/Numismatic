import unittest

import coin

class NominalPropertyTest(unittest.TestCase):	
	def test_coin_creation(self):
		test_coin = coin.Coin(10)
		self.assertEqual(test_coin.nominal, 10)
		
	def test_nominal_property_setter(self):
		test_coin = coin.Coin(10)
		test_coin.nominal = 5
		self.assertEqual(test_coin.nominal, 5)

if __name__ == '__main__':
    unittest.main()