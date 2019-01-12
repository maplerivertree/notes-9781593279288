# if:
# if: & n elif:
# if: & else:
# if: & n elif: & else:

l = list(range(1,6,1))

if 7 in l:
	print('7 is in the list')
elif 3 not in l:
	print('8 is in the list')
else:
	print('only ' + str(l) + ' is in the list')


count=0
for i in l:
	count=count+1
	if i == 9:
		print('the list contains this number')
		count=count-1
	elif count==len(l):
		print('the list does not contain this number')
