import sqlite3


connection=sqlite3.connect('customer.db')

cur=connection.cursor()

#create a table

cur.execute(""" CREATE TABLE customers (
  first_name text,
  last_name text,
  email text
)


	""")
#commit our command
connection.commit()

#close our connection
connection.close()