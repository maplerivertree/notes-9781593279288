#dictionaries
#anatomy, addition, modification


#use ":" NOT "=" for key-value pairing

robot1 = {'fraction': 'police', 'weapon': 'uzi', 'x-axis': 4, 'y-axis': 5}
robot2 = {'fraction': 'terrorist', 'weapon': 'ak47', 'x-axis': 2, 'y-axis': 25}
print('robot1 ' + str(robot1))
print("robot2's weapon is " + str(robot2["weapon"]))

#addition; use squre bracket [] and an "=" assignment
#this addition is really easy to forget
robot1['HP'] = 100
print('robot1 ' + str(robot1))

#modification
robot2['x-axis'] = 5
print('robot2 ' + str(robot2))
