#tuples

# a list
l = [1,3,-3,6]
# a tuple
t = (1,3,-3,6)

l[0] = 5
print(l)
t[0] = 5
print(t) # this will return error because a tuple is immutable
