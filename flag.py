
#flag continue break   while True
#while True will continue to run until it reaches a 'break'
print("\n\nGame Rule: \n\tYou need to type in the result of 1x13, 2x13, 3x13, and etc.")
print("\tYou have 3 chances.")
print("\tIf you type in a negative number --- instant gameover.")
print("\tType 'quit' to exit")

count = 1
scores = 0

chances = 3
Game_on = True

user_input_his = [-2,-1,0]

while Game_on and chances >0:
		scores = scores + 1
		print('\nYour current score is: '+ str(scores))
		print('You still have '+str(chances)+' chances.')
		print(user_input_his)
		user_input=input('Your next input: ')

		if user_input=='quit':
			print("Now quiting... Thanks for playing.")
			break

		user_input=int(user_input)
		user_input_his.append(user_input)

		
		if user_input % 13 != 0 and user_input>0:
			chances = chances - 1
			if chances == 0:
				print('No more chances. Game Over.')
				Game_on = False
			print("not a module of 13, please start from 13 again")
			scores = scores - 1
			continue

		elif user_input_his[-1] <= user_input_his[-2] and user_input > 0:
			chances = chances - 1
			if chances == 0:
				print('No more chances. Game Over.')
				Game_on = False
			print("You entered with reversed order.")
			scores = scores - 1
			continue

		elif user_input < 0:
			print("Instant Game Over.")
			Game_on = False

