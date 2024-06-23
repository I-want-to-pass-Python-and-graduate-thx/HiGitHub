#Define X=?, Y=?
X = int(input("Enter X: "))
Y = int(input("Enter Y: "))
#Number:數字；Bound:上限
if X <= Y:
	Number = X
	Bound = Y
else: # X>Y
	Number = Y
	Bound = X
#The number <= the bound through the if&else loop, so line 14 always be true.

result="" #An empty string to accomodate the number
while Number<=Bound:
	if (number % 13 == 0) and (number % 7 == 0): # % means divide.
		result = result + str(number)+" "
		number +=1
print(result)