import sqlite3


connection=sqlite3.connect('customer.db')

cur=connection.cursor()

#update records
cur.execute("""

UPDATE customers SET first_name='BOB' 
WHERE last_name='shifat'


	""")

connection.commit()


#fetch data
cur.execute(" SELECT * FROM customers")
data=cur.fetchall()

for item in data:
	print(item)

connection.commit()










connection.commit()
print("database command executed!")
connection.close()