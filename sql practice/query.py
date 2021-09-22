import sqlite3


connection=sqlite3.connect('customer.db')

cur=connection.cursor()

#insert data

#make query

cur.execute("SELECT rowid,* FROM customers")

data=cur.fetchall()
#print("Full Name"+"\t\t\tEmail")
print("--------------------------")
for item in data:
 #print(item[0]+"\t"+item[1]+"\t\t"+item[2])
 #print("---------------------------------")
 print(item)
 






connection.commit()
print("database command executed!")
connection.close()