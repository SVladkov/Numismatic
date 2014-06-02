import sqlite3
import idatabase

class SQLiteDatabase(idatabase.IDatabase):
	def __init__(self):
		self.connection = sqlite3.connect('sqlite_coin_database.db')
		self.cursor = self.connection.cursor()

	def tableCreate(self):
		self.cursor.execute("CREATE TABLE stuffToPlot(nominal INTEGER, year INTEGER)")
	
	def enter_coin(self, coin):
		self.cursor.execute("INSERT INTO stuffToPlot (nominal, year) VALUES(?, ?)", 
						(coin.nominal, coin._year))
		self.connection.commit()
		
	'''sql = "SELECT * FROM stuffToPlot WHERE age =?"
	wordUsed = 24 
		
		
	def readData(self):	
		for row in cursor.execute(sql, [(wordUsed)]):
			print(row)
	'''
#SQLiteDatabase.tableCreate()
	#dataEntry()
	#readData()


	