# .sort()  .sort(reverse=True)  sort(listname,reverse=True)  .reverse()
cars=['a','c','b']
print('original list ' + str(cars))

# sort(); permenant
cars.sort(reverse=True)
print(cars)
cars.sort()
print(cars)

# .reverse
cars.reverse()
print(cars)

# sorted(listname) is temp sort
print(sorted(cars,reverse=True))

