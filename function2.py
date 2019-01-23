#positional argument, keyword argument

def make_a_point(a, b):
	return(a + ' catch ' + b +".")

#positional arguments. The input order matters
print(make_a_point('cats', 'mice'))
print(make_a_point('mice', 'cats'))

#keyword arguments
print(make_a_point(b = 'mice', a = 'cats'))