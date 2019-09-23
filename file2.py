
# file_append_mode

filepath = "a.txt"

with open(filepath, 'a') as file_object:
	file_object.write("appending this sentence to the existing file.")


