#while loop to generate 9X9 multiplication table
#the 1st part of the table
m, n=9, 9
while 1<=m<=9:
	while n>0:
		print(m, "x", n, "=", m*n, end = "\t")
		print(m, "x", (n-1), "=", m*(n-1), end = "\t")
		print(m, "x", (n-2), "=", m*(n-2), end = "\n")
		m=m-1
		if m==0:
			break
print()

#the 2nd part of the table
i, j=9, 6
while 1<=i<=9:
	while j>0:
		print(i, "x", j, "=", i*j, end = "\t")
		print(i, "x", (j-1), "=", i*(j-1), end = "\t")
		print(i, "x", (j-2), "=", i*(j-2), end = "\n")
		i=i-1
		if i==0:
			break
print()

#the 3rd part of the table
a, b=9, 3
while 1<=a<=9:
	while b>0:
		print(a, "x", b, "=", a*b, end = "\t")
		print(a, "x", (b-1), "=", a*(b-1), end = "\t")
		print(a, "x", (b-2), "=", a*(b-2), end = "\n")
		a=a-1
		if a==0:
			break