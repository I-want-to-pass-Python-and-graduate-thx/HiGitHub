# Richter scale conversion

# Get the value to convert
richter_scale =float(input("Please input a Richter scale value:")) 
print(richter_scale)

# Determine conversion and display results
if richter_scale >0:
		converted_scale = 10^((1.5*richter_scale)+4.8)
		TNT_value = converted_scale*4.184*10^9
		number_of_nutritious_lunches = TNT_value/2930200
		print("Equivalence in Joules:", converted_scale, "Equivalence in tons of TNT:", TNT_value, "Equivalence in the number of nutritious lunches:", number_of_nutritious_lunches)