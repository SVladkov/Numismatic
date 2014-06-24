import coin
import country
import sqlite_database
import idatabase

def push_test_data():
	test_database = sqlite_database.SQLiteDatabase()
	
	test_coin = coin.Coin(5, country.test_country, 1976)	
	test_database.enter_coin(test_coin)	
	
	test_coin = coin.Coin(5, country.test_country, 1985)	
	test_database.enter_coin(test_coin)	
	
	test_coin = coin.Coin(10, country.test_country, 1976)	
	test_database.enter_coin(test_coin)	
	
push_test_data()