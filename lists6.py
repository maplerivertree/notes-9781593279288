#list comprehension
#https://docs.python.org/3/tutorial/datastructures.html?highlight=list%20comprehension

L = [i/2 for i in range(-3,19,2)]
print(L)


from math import *
L2 = [str(round(pi,i)) for i in range(1,7,1)]
print(L2)