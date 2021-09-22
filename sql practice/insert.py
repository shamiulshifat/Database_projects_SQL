import sqlite3


connection=sqlite3.connect('customer.db')

cur=connection.cursor()

many_customers=[('wes', 'brown', 'hel@gmail'),
 ('hhhh', 'hdhdhhd', 'gddhdhd'), 
 ('jhddjh', 'dhjdhjdh', 'dhdhdd')
          
]

cur.executemany("""

INSERT INTO customers VALUES(?,?,?)


	""", many_customers)
connection.commit()
print("database updated")
connection.close()