import database


MENU_PROMT="""
--coffee bean app--

please choose one of the options:

1) add a new bean.
2) see all bean.
3) find a bean by name.
4) see which preparation method is the best for a bean.
5)Exit.

Your SELECTION:
"""

def menu():
	connection=database.connect()
	database.create_tables(connection)
	while(user_input :=input(MENU_PROMT)) !="5":
		if user_input== "1":
			name=input("enter bean name:")
			method=input("enter method:")
			rating=int(input("enter rating:"))

			database.add_bean(connection,name,method,rating)
		elif user_input== "2":
			beans=database.get_all_beans(connection)

			for bean in beans:
				print(f"{bean[1]} ({bean[2]})- {bean[3]}/100")

		elif user_input== "3":
			name=input("enter bean name:")
			beans=database.get_beans_by_name(connection, name)

			for bean in beans:
				print(f"{bean[1]} ({bean[2]})- {bean[3]}/100")

		elif user_input== "4":
			name=input("enter prep method:")
			best_method=database.get_best_preparation_for_beans(connection, name)

			print(f"The best prep method for {name} is : {best_method[2]}")
			#print(best_method)



		else:
			print("invalid input given.")





menu()