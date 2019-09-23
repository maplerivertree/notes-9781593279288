# try, except, else


print("Give me two numbers, and I'll divide them.")
print("Enter '1'to quit.")

while True:
	num1 = input("/First number: ")
	if num1 == 'q':
		break
	num2 = input("Second number: ")

	try:
		answer  = int(num1) / int(num2)
	except ZeroDivisionError:
		print("Zero Division Error")
	else:
		print(answer)
