import sqlite3
import idatabase

class SQLiteDatabase(idatabase.IDatabase):
	def __init__(self):
		self.connection = sqlite3.connect('sqlite_coin_database.db')
		self.cursor = self.connection.cursor()

	def table_create(self):
		self.cursor.execute("CREATE TABLE coin_table(nominal INTEGER, year INTEGER)")
	
	def enter_coin(self, coin):
		self.cursor.execute("INSERT INTO coin_table (nominal, year) VALUES(?, ?)", 
						(coin.nominal, coin._year))
		self.connection.commit()

	def get_by_year(self, year):
		sql = "SELECT * FROM coin_table WHERE year = ?"
		coins = []
		for row in self.cursor.execute(sql, [(year)]):
			coins.append(row) 
		return coins	
	
test_database = SQLiteDatabase()

print(test_database.get_by_year(1976))