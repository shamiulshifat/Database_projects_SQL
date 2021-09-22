import sqlite3


connection=sqlite3.connect('customer.db')

cur=connection.cursor()
#insert a data
#cur.execute("INSERT INTO customers VALUES('shamiul', 'medha', 'shifat')")
#connection.commit()
#we search for specific things on db
cur.execute("SELECT * FROM customers WHERE last_name LIKE '%at'")

data=cur.fetchall()
print(data)











connection.commit()
print("database command executed!")
connection.close()