#p24
#presidents = ['Bush', 'CLinton', 'Bush', 'Obama']
#print("---".join(presidents))

#p27 In-class Exercise
#"From h1234567@ncku.edu.tw Tue Sep 27 10:14:16 2016" to "Tue Sep 27 10:14:16 2016 From h7654321@ncku.edu.tw" 
#data = 'From h1234567@ncku.edu.tw Tue Sep 27 10:14:16 2016'
#pos1 = data.find('h')
#pos2 = data.find('@')
#data = data[:pos1+1] + "7654321"+ data [pos2:] #'print out From h'，not included any empty strings.
#also with email address
#pos3 = data.find('Tue')
#modified_data = data[pos3:]+" "+ data[:pos3]
#print(modified_data) 

#p28_formatting string
format ="My name is %s and height is %d cm!"
values =("John", 170)
print(format % values)

#p29_formatting the string(non)
#print("My name is %s " % ('Zara'))
 #%s : string  ‐‐> My name is Zara 
#print("My weight is %d kg and my height is %d cm!" % (61, 165))
 # %d : decimal integer  ‐‐> My weight is 21 kg!
 #print("Now is %d degree, my name has %d characters" % (‐21, len("Zara")))
 # %c : character  ‐‐> Now is ‐21 degree, My name has 4 characters 
#print("The temperature is %f degrees precisely" % (‐21.34))
 # %f : floating point real number
 # ‐‐> The temperature is ‐21.340000 degrees precisely
 #print("My BMI is %f " % ((50/(170/100)**2)))
 # you also can use expression as the value ‐‐> My BMI is 17.301038 
#print("%d big numbers: %e %e" % (2, 123456789, 999999999999999999999))
 # %e : exponential notation (with lowercase 'e')
 # ‐‐> big number 1.234568e+08 1.000000e+21
#print("another big number %E" % (987654321))
 # %E : exponential notation (with UPPERcase 'E')
 # ‐‐> another big number 9.876543E+08