#function5
# pass an arbituary number of arguments


# create an initial list of policemen (a list of dictionaries)
db=[]
for i in range(1,5,1):
	robot = {'fraction' : 'police', 'HP' : 100}
	db.append(robot)
for i in db[:3]:
	print(str(i))
print('\n')


#--- a function that allows user to add 
def propagate(current_db, fraction, health, num_of_addition, **other):
	for i in range(1,num_of_addition,1):
		robot = {'fraction': fraction, 'HP': health}
		for v, k in other.items():
			robot[v] = str(k)
		current_db.append(robot)
	
	return(current_db)
#---

# ask user to add more characters to the game

f = input('What type of characters you wish to add? (policemen/terrorist): ')
n = input('How many to add? (1-10): ')
h = input("What's the health for these characters>? (1-100): ")
s = input("What's a superpower for them? :")
w = input('What weapon do they carry? :')


propagate(db, str(f), int(h), int(n),
	superpower = str(s), 
	weapon = str(w)
	)

for i in db[:]:
	print(str(i))






	


#user_info = {'Name':'Kate', 'Age':20}


#def store_info(existing_info, Name, Age, **Other):
















