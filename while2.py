#while2 move from one list to another

stomach= []
fridge = ['eggs','grapes','steak','pasta']

print("What is in the stomach: " + str(stomach))
print("What is in the fridge: "+ str(fridge))

#WHILE list-name:
while fridge:
	stomach.append(fridge.pop())


print("What is in the stomach: " + str(stomach))
print("What is in the fridge: "+ str(fridge))