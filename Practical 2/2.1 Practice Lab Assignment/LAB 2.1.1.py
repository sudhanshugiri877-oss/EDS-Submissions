lst=[]

while True:
	print("1. Add")
	print("2. Remove")
	print("3. Display")
	print("4. Quit")

	choice=input("Enter choice: ")

	if choice=='1':
		val=input("Integer: ")
		if val.lstrip('-').isdigit():
			lst.append(int(val))
			print("List after adding:",lst)
		else:
			print("Invalid input")

	elif choice =='2':
		if not lst:
			print("List is empty")
		else:
			val=input("Integer: ")
			if val.lstrip('-').isdigit():
				val=int(val)
				if val in lst:
					lst.remove(val)
					print("List after removing:",lst)
				else:
					print("Element not found")
			else:
				print("Invalid input")

	elif choice =='3':
		if not lst:
			print("List is empty")
		else:
			print(lst)

	elif choice =='4':
		break

	else:
		print("Invalid choice")