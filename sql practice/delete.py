import sqlite3


connection=sqlite3.connect('customer.db')

cur=connection.cursor()

#delete records
cur.execute("""

DELETE FROM customers WHERE first_name='medha'



	""")

connection.commit()


#fetch data
cur.execute(" SELECT * FROM customers")
data=cur.fetchall()

for item in data:
	print(item)








connection.commit()
print("database command executed!")
connection.close()