import database


menu_prompt= """

--Welcome to Shifat's Dine---

Please select an option:

1) Menu & order
2) View My order
3)View all order
4)Exit

"""


def fullmenu():
    connection=database.connect()
    database.create_table_order(connection)

    while (user_input := input(menu_prompt)) !="4":
    	if user_input== "1":
    		name=input("Enter your name: ")
    		rice=input("enter rice quantity: ")
    		curry=input("enter curry quantity: ")
    		coke=input("enter coke quantity: ")
    		price=(100*int(rice))+(200*int(curry))+(20*int(coke))
    		database.add_orders(connection, name, rice, curry,coke, price)

    	elif user_input=="2":
    		name=input("Enter your name: ")
    		data=database.show_orders(connection, name)
    		print(f"{data[1]}\t ordered- Rice: {data[2]}\t Curry: {data[3]}\t Coke: {data[4]}\t --Total Bill: {data[5]}")


    	elif user_input=="3":
    		data=database.show_all_orders(connection)

    		for item in data:
    			print(f"{item[1]}\t ordered- Rice: {item[2]}\t Curry: {item[3]}\t Coke: {item[4]}\t --Total Bill: {item[5]}")

    	else:
    		print("invalid button pressed")





fullmenu()
