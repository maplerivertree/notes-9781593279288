#input list preservation for function processing

user_SSN = [9923278945,6623526436,286634234,7776463453,2162342365]
encrypted_SSN = []

print(str(user_SSN))
print(str(encrypted_SSN))


def encryption(input_list):
	output_list= []
	while input_list:
		output_list.append(input_list.pop()/33)
	return output_list



# USING [:] to preserve the input_list
print(str(encryption(user_SSN[:])))
print(str(user_SSN))

# without [:]
print(str(encryption(user_SSN)))
print(str(user_SSN))

 

