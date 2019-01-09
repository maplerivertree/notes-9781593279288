#lists5 
# range(*,*,*) list(range()) use loop&append to create a list

#Important: don't forget the colon, be cautious with indention.
pizzas=['hawaii','feastive','vegan']
for pizza in pizzas:
	print('I like ' + pizza +'\t.')
print('\tThat is it.')

for i in range(1,6,1):
	print(i)
print('\n')

a = list(range(1,16,3))
for i in a:
	print(i)

b = []
for i in range(1,20,4):
	b.append(i**2)
print(b)