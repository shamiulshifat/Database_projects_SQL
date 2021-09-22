import sqlite3

#initiate database
def connect():
 return sqlite3.connect("data.db")

#create a table for saving orders
create_table_orders="CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, name TEXT, rice INTEGER, curry INTEGER, coke INTEGER, price INTEGER)"

#add data to order
insert_orders="INSERT INTO orders (name, rice, curry,coke, price) VALUES(?,?,?,?,?)"

#show my orders
my_orders="SELECT * FROM orders where name=?"

def create_table_order(connection):
 with connection:
	 connection.execute(create_table_orders)


def add_orders(connection, name, rice, curry,coke, price):
	connection.execute(insert_orders,(name, rice, curry,coke, price))


def show_orders(connection, name):
	with connection:
		return connection.execute(my_orders, (name,)).fetchone()



def show_all_orders(connection):
	with connection:
		return execute("SELECT * FROM orders").fetchall()