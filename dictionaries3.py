#dictionaries3
#propagate 'a LIST of DICTIONARIES'
robots = []
for i in range(1,500,1):
	robot = {'fraction': 'policy', 'weapon': 'm4a', 'HP': 100}
	robots.append(robot)

for robot in robots[0:3]:
	print(robot)
print('...')
