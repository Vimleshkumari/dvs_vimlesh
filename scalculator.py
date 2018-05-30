def addition(a,b):	
	return a+b
def substraction(a,b):
	return a-b
def multiply(a,b):
	return a*b
def division(a,b):
	return a/b
def modolus(a,b):
	return a%b
num1=int(input('print first no'))
num2=int(input('print second no')) 
print("Please select operation -\n" 	
		"1. Add\n" 
		"2. Subtract\n" 
		"3. Multiply\n" 
		"4. Divide\n")

select =input("Select operations form 1, 2, 3, 4 :")

if select == '1':
	print(num1, "+", num2, "=",
			+		add(num1, num2))

elif select == '2':
	print(num1, "-", num2, "=",
					subtract(num1, num2))

elif select == '3':
	print(num1, "*", num2, "=",
					multiply(num1, num2))

elif select == '4':
	print(num1, "/", num2, "=",
					divide(num1, num2))
else:
	print("Invalid input")
