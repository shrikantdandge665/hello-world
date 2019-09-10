import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "shrikant2",
	database = "studentdb",
	)
my_cursor  = mydb.cursor()
