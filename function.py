#function
import math


def sqr(num=2):
	sqr_num = math.sqrt(num)
	return sqr_num

user_input=int(input("Squre Root Calculator Input Number: "))
print('Answer: ' + str(sqr(user_input)))