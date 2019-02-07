#files

#READ, .rstrip()
filename = 'a.txt'
with open(filename) as file_object:
	content = file_object.read()
	print(content.rstrip())
	"""w/o .rstrip(), .read() append one additional blank line"""

#absolute path
"""USE forward slash / for file path, because 
backward slash is used as escape, e.g. \n"""
filename='f:/b/c.txt'
with open(filename) as file_object:
	content = file_object.read()
	print(content.rstrip())

#Store file line by line as a list by using .readlines()
filename = 'a.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

for i in lines:
	if 'analysis' in i:
		print(i.rstrip())