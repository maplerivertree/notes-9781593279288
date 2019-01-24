# function ingests a list


import math
def square_root(input_list):
	output_list = []
	for i in input_list:
		i = math.sqrt(i)
		output_list.append(i)

	return output_list
#--
training_set_a = [2,3,4,5,6,7,8,9]
print(str(square_root(training_set_a)))
















