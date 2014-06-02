import unittest
import idatabase
import sqlite_database
import country
import coin

class DatabaseTest(unittest.TestCase):	
	def test_database_connection(self):
		test_database = sqlite_database.SQLiteDatabase()
		test_coin = coin.Coin(5, country.test_country, 1976)
		test_database.enter_coin(test_coin)
		
		
if __name__ == '__main__':
    unittest.main()