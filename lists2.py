

inside_fridge=['gin','bread','pizza','vodka','lillet','bitter','rum','egg','cheesecake','milk','juice']

# 2 ways to delet

# del , delete by position
print('delete, delete by position')
del inside_fridge[4]
print(inside_fridge)
# remove, remove by value
print('remove, remove by value')
inside_fridge.remove('bitter')
print(inside_fridge)


expired_items = 'bread'
inside_fridge.remove(expired_items)
print(inside_fridge)



lunch = inside_fridge.pop(-3)
print("what you had for lunch is " + str(lunch) + ", and what's left in the fridge is " + str(inside_fridge))