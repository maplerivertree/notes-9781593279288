#lists & title()

bikes=['trek','giant','specialized','canyan']
print(bikes[3])
print(bikes[3].upper())
print(bikes)
bikes[0] = "generic"
print(bikes)


#pop()
#\n is used to be within an apostrophe
#str to allow a print of a list
print("#pop")
popped_bikes = bikes.pop()
print(str(bikes) + "\nThe popped item is " + str(popped_bikes))



#insert(0,)
bikes.insert(1,'between generic and giant')
print(bikes)

#append()
bikes.append('trek')
print(bikes)

#  to run in CL; E:\python_crash> python lists.py 
 
