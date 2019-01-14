# loop by .items(), .keys(), values(), set()
print('\n')
best_discipline = {
	'emily': 'swim', 
	'mary': 'swim', 
	'bob': 'bike', 
	'joshua': 'swim', 
	'rogers': 'run',
	'poco': 'basketball',
	'joe': 'ski',
	'annika': 'run'
	}
triathlon = ['swim', 'bike', 'run']

print(best_discipline)
print(triathlon)
print(best_discipline['joshua'].upper())


print("loop by pairs, by keys, by values")
#LOOP by PAIRS
for k, v in best_discipline.items():
	if v in triathlon:
		print(str(v).title() + ' is a triathlon sport.')

print('\n\tLoop all keys')
for name in best_discipline.keys():
	print('\t' + str(name))

print('\n\tLoop all keys sorted')
for name in sorted(best_discipline.keys()):
	print('\t' + str(name))

print('\nLoop all value:')
for discipline in best_discipline.values():
	print('\t\t' + str(discipline))

#DISTINCT; review the brackets arrangements for .value() and set()
print('\nLoop all distinct value:')
for discipline in set(best_discipline.values()):
	 print('\t\t' + str(discipline))





