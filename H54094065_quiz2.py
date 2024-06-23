#input the shopping amount
shopping_amount=int(input("Enter the shopping amount:")) 
#check the membership level to identify how much is the discount
membership_level=str(input("Enter the membership level:"))
#calculate the discount base on the membership level and shopping amount
if membership_level =="Gold":
	if shopping_amount >1000:
		discount_shopping_amount=shopping_amount*0.85
		print("membership_level", "$", discount_shopping_amount)
	elif shopping_amount>1500:
		discount_shopping_amount=shopping_amount*0.8
		print("membership_level", "$", discount_shopping_amount)
	elif shopping_amount >3000:
		discount_shopping_amount=shopping_amount*0.75
		print("membership_level", "$", discount_shopping_amount)
	else:
		print("membership_level", "$", shopping_amount)
elif membership_level == "Regular":
	if shopping_amount >1000:
		discount_shopping_amount=shopping_amount*0.9
		print("membership_level", "$", discount_shopping_amount)
	elif shopping_amount>1500:
		discount_shopping_amount=shopping_amount*0.85
		print("membership_level", "$", discount_shopping_amount)
	elif shopping_amount >3000:
		discount_shopping_amount=shopping_amount*0.8
		print("membership_level", "$", discount_shopping_amount)
	else:
		print("membership_level", "$", shopping_amount)
#The customer won't get any discount if the membership level is neither "Gold" or "Regular"
else membership_level != "Gold" or membership_level!= "Regular":
	print("Invalid membership level. Please enter 'Regular' or 'Gold'.")
