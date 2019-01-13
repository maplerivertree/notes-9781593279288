#if2
#compare lists
L1 = ['a', 'b', 'c', 'd', 'e']
L2 = ['e', 'f', 'g', 'a']
L3 = ['b', 'eg', 'ege', 'a', 'egee']
print(L1)
print(L2)
print(L3)

for i in L2:
	if i in L1:
		if i in L3:
			print(str(i) + ' is in all 3 lists')
		else:
			print(str(i) + ' is in list1 and list2')
	elif i in L3:
			print(str(i) + ' is in list1 and list3')
	else:
		print(str(i) + ' is only in list1')
