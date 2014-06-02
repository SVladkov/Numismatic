import sqlite3
import idatabase

class SQLiteDatabase(idatabase.IDatabase):
	def __init__(self):
		self.connection = sqlite3.connect('sqlite_coin_database.db')
		self.cursor = self.connection.cursor()

	def table_create(self):
		self.cursor.execute("CREATE TABLE coin_table(nominal INTEGER, year INTEGER)")
	
	def enter_coin(self, coin):
		self.cursor.execute("INSERT INTO stuffToPlot (nominal, year) VALUES(?, ?)", 
						(coin.nominal, coin._year))
		self.connection.commit()

	def get_by_year(self, year):
		sql = "SELECT * FROM coin_table WHERE year = ?"
		coins = []
		for row in cursor.execute(sql, [(year)]):
			coins.append(row + "\n")
		return coins	