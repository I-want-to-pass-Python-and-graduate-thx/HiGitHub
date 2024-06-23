#score = int(input("Please enter a score: "))
#if 0 <= score <= 49:
	#print("Inadequate")
#if 50 <= score <= 59:
	#print("Marginal")
#if 60 <= score <= 69:
	#print("Adequate")
#if 70 <= score <= 79:
	#print("Good")
#if 80 <= score <= 89:
	#print("Exceptional")
#if 90 <= score <=100:
	#print("Outstanding")

#P34 in-class exercise pH level
myinput = input("pH value: ") #此時輸入值會被作為字串對待
if len(myinput) > 0: #字串長度是否大於0
	ph = float(myinput) #若大於0，則將此字串轉換為浮點數，並指定為ph值
	if ph < 0 or ph >15.0:
		print("Invalid pH value.")
	elif 0<= ph <5:
		print("Strong acid")
	elif 5<= ph <7:
		print("Weak acid")
	elif 7<= ph <8:
		print("Neutral")
	elif 8<= ph <10:
		print("Weak base")
	else:
		print("Strong base")
else:
		print("No pH value given.")

#P35 Fahrenheit and Celsius Conversion Program
print("This program will convert temperatures (Celsius/Fahrenheit)")
print("Enter (F) to convert Fagrenheit to Celsius")
print("Enter (C) to convert Celsius to Fahrenheit")

#Get temperature to convert
which = input("Enter selection: ")
= (
#