print("Welcome to the simple calculator program!")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

#perform another operation
another = str(input("Do you want to perform another calculation? (yes or no): "))
if another == "yes":
	print("Welcome to the simple calculator program!")
	print(first_number, /n second_number)
if another == "no":
	print ("Goodbye!")

if enter_the_operation == "+":
	print("Result: ", first_number+second_number, \n )
elif enter_the_operation == "-":
	print("Result: ", first_number-second_number)
elif enter_the_operation == "*":
	print("Result: ", first_number*second_number)
elif enter_the_operation == "/":
	print("Result: ", first_number/second_number)
else:


#enter an arithmetic operation to continue
enter_the_operation = str(input("Select an arithmetic operation (+, -, *, /): "))
#print out the results
if enter_the_operation == "+":
	print("Result: ", first_number+second_number, \n )
elif enter_the_operation == "-":
	print("Result: ", first_number-second_number)
elif enter_the_operation == "*":
	print("Result: ", first_number*second_number)
elif enter_the_operation == "/":
	print("Result: ", first_number/second_number)
else:
	print(another)