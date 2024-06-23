def func():
def calc_circumference(radius):
#定義周長

def print_lyrics():
	print("Jjj jj jj all the way")
	print('wish you a merry ...')

#呼叫:直接輸入即可
print_lyrics()

#函數的argument可以放在括號裡
def func2(x, y, z):
	#一定要定義多少用多少
	added = x+y+z
	return added
#函數能夠被定義為變數，變數只要把函數填空就好
x= func2(3, 4, 5)
print(x)

#p16，看懂上面計算過程
def square(n):
	return n ** 2
num = int(input("Please enter an integer"))
#能夠算出平方的結果
result = square(num)
print(result)

#p17
def celsius_to_fahr(celsuis):
	#Return Fahrrenheit equivalent to given temperature
	fahr=celsuis*9/5+32
	return fahr
for temp in range(-10, 50, 5):
	print(temp, "C= ", celsuis_to_fahr(temp), "F")

#p18 Program Strucure
#第一~第二個function是先定義你要用的函數
def func1(...):
	#寫你要用這函數幹嘛
	print("blablabla")
def func1(...):
	print("abcabc")
#然後可以寫下其他的function defs
#下面才是主程式邏輯部分，包含function calls
staTEMENTS 
variable assignments
func1(...) #呼叫函數1
func2(...) #呼叫
#重點，若你使用一組程式碼超過一次，就能夠去試著把他寫成函數

